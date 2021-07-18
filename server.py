#! /usr/bin/python
# coding: utf-8

import linecache
import random
import socket, sys
import threading
import json
import re
import traceback
import uuid
import emoji
from types import request_types, response_types, error_types
import database
import utility

import models.user_model as user_model
import models.game_request_model as game_request_model
import models.minroob_model as minroob_model

connections = []
global_db = None

ROW_COUNT = 8
COL_COUNT = 8
BOMBS_BUTTON = 1
EMPTY_BUTTON = -1
RECV_BUFFER = 1024 * 10  # fairly arbitrary buffer size, specifies maximum data to be recieved at once

local_db_setting = {
    'username': "root",
    'password': None,
    'host': '127.0.0.1',
    'dbname': 'minroob',
}

server_db_setting = {
    'username': "root",
    'password': 'test',
    'host': '127.0.0.1',
    'dbname': 'minroob',
}
HOST = "test.com"
db_setting = server_db_setting

class Client(threading.Thread):
    def __init__(self, socket, address, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = None
        self.signal = signal
        self.user = None
        self.auth = None
        self.db = database.Db(username=db_setting['username'], password=db_setting['password'], host=db_setting['host'], dbname=db_setting['dbname'])
        # self.db.watch()

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # Attempt to get data from client
    # If unable to, assume client has disconnected and remove him from server data
    # If able to and we get data back, print it in the server and send it back to every
    # client aside from the client that has sent it
    # .decode is used to convert the byte data into a printable string

    def remove_uni(self, s):
        """remove the leading unicode designator from a string"""
        if s.startswith("u'"):
            s2 = s.replace("u'", "'", 1)
        elif s.startswith('u"'):
            s2 = s.replace('u"', '"', 1)
        else:
            s2 = s
        return s2

    def send_message(self, message):
        try:
            string_unicode = emoji.emojize(str("" + message + "\r\n")).replace("u'", "'").encode('utf-8')
            self.socket.send(string_unicode)
        except:
            connections.remove(self)

    def send_json(self, gson):
        self.send_message(json.dumps(gson, ensure_ascii=False))

    def send_json_to_other(self, gson):
        broadcast_data(json.dumps(gson))

    def send_error(self, code, message):
        self.send_message(json.dumps({
            "status": "error",
            "code": code,
            "message": message
        }))

    def send_reply(self, type, data):
        self.send_json({
            'status': response_types.OK,
            'type': type,
            'data': str(data)
        })

    def find_opposing_player_id(self, game):
        if game[minroob_model.PLAYER_ONE_ID] == self.user[user_model.USER_ID]:
            opposing_player_id = game[minroob_model.PLAYER_TWO_ID]
        else:
            opposing_player_id = game[minroob_model.PLAYER_ONE_ID]
        return opposing_player_id

    def create_account(self, gson):
        username = gson['username']
        password = gson['password']
        password2 = gson['password2']
        fullname = gson['fullname']
        if len(username) < 5:
            self.send_error(error_types.ERROR_SIGN_UP, "username is too short")
            return

        if fullname == "":
            self.send_error(error_types.ERROR_SIGN_UP, "fullname must not be empty")
            return

        if len(password) < 5:
            self.send_error(error_types.ERROR_SIGN_UP, "password is too short")
            return

        if password != password2:
            self.send_error(error_types.ERROR_SIGN_UP, "password is not match by password2")
            return

        token = str(uuid.uuid1())
        self.db.create_account(username, password, fullname, token)
        self.check_auth({
            'login_by': 'token',
            'token': token
        })

    def get_running_game(self):
        alive_game = self.db.get_running_game(self.user[user_model.USER_ID])
        if alive_game is not None:
            status, opposing_player = self.db.get_player_by_id(self.find_opposing_player_id(alive_game))
            self.send_reply(response_types.RESUME_GAME, {
                'player_name': opposing_player[user_model.USER_NAME],
                'game_id': alive_game[minroob_model.GAME_ID]
            })
            return True
        else:
            return False

    def change_player_status(self, status):
        if self.user is None:
            return

        self.db.set_player_status(self.user[user_model.USER_ID], status)
        broadcast_json(response_types.PLAYER_STATUS, {
            'player': {
                'id': self.user[user_model.USER_ID],
                'fullname': self.user[user_model.FULLNAME],
                'username': self.user[user_model.USER_NAME],
            },
            'is_online': utility.to_json_bool(status),
        }, [self.user[user_model.USER_ID]])
        if status:
            game_request = self.db.get_waiting_game_request(self.user[user_model.USER_ID])
            if game_request is not None:
                self.db.remove_waiting_game(game_request[game_request_model.ID])
                self.send_reply(response_types.START_GAME, {
                    'game_id': game_request[game_request_model.ID]
                })
                connection = get_connection_by_user_id(game_request[game_request_model.RECEIVER_PLAYER_ID])
                connection.send_reply(response_types.START_GAME, {
                    'game_id': game_request[game_request_model.ID]
                })

    def check_auth(self, gson):
        if (gson['login_by'] == "token"):
            status, user = self.db.get_player_by_token(gson['token'])
        else:
            status, user = self.db.get_player_by_userpass(gson['username'], gson['password'])

        if status:
            self.auth = True
            self.user = user
            self.change_player_status(True)
            self.send_reply(
                response_types.TYPE_USER,
                {
                    'id': user[user_model.USER_ID],
                    'fullname': user[user_model.FULLNAME],
                    'username': user[user_model.USER_NAME],
                    'token': user[user_model.USER_TOKEN]
                }
            )
        else:
            self.send_error(error_types.ERROR_FAIL_AUTH, "fail_auth")

    def stop_self(self):
        self.signal = False
        self.socket.close()
        self.db.close()
        self.change_player_status(False)
        connections.remove(self)
        print("must Stop client")

    def add_message(self, gson):
        self.db.add_message(self.user[user_model.USER_ID], gson['message'])
        self.send_json_to_other({
            'status': 'ok',
            'type': response_types.NEW_MESSAGE,
            'name': self.user[user_model.USER_NAME],
            'message': gson['message'],
            'profile_image': self.user[user_model.PROFILE_IMAGE]
        })

    def add_global_message(self, gson):
        player_id = self.user[user_model.USER_ID]
        message = gson['message']
        self.db.add_global_message(player_id, message)
        broadcast_json(response_types.NEW_GLOBAL_MESSAGE, {
            'player_id': player_id,
            'fullname': self.user[user_model.FULLNAME],
            'message': message,
            'timestamp': utility.get_current_timestamp(),
        })

    def game_request(self, gson):
        self.db.remove_game_request(self.user[user_model.USER_ID], gson['player_id'])
        self.db.add_game_request(self.user[user_model.USER_ID], gson['player_id'])
        self.get_outgoing_game_request()
        connection = get_connection_by_user_id(gson['player_id'])
        if connection is not None:
            connection.get_incoming_game_request()

    def get_incoming_game_request(self):
        game_requests = self.db.get_incoming_game_request(self.user[user_model.USER_ID])
        self.send_reply(response_types.INCOMING_GAME_REQUEST, game_requests)

    def get_outgoing_game_request(self):
        game_requests = self.db.get_outgoing_game_request(self.user[user_model.USER_ID])
        self.send_reply(response_types.OUTGOING_GAME_REQUEST, game_requests)

    def get_online_players(self):
        players = self.db.get_online_players(self.user[user_model.USER_ID])
        self.send_reply(response_types.ONLINE_PLAYERS, players)

    def cancel_game_request(self, gson):
        status, receiver_player_id = self.db.get_receiver_play_id_by_game_id(gson['game_id'])
        self.db.cancel_game_request(gson['game_id'])
        self.get_outgoing_game_request()
        if status:
            connection = get_connection_by_user_id(receiver_player_id)
            if connection is not None:
                connection.get_incoming_game_request()

    def accept_game_request(self, gson):
        game_id = gson['game_id']
        status, game_request = self.db.get_game_request_by_id(game_id)
        if status:
            print("line 157")
            sender_player_id = game_request[game_request_model.SENDER_PLAYER_ID]
            connection = get_connection_by_user_id(sender_player_id)
            if connection is None:
                self.db.add_waiting_game(game_id)
                status, sender_player = self.db.get_player_by_id(sender_player_id)
                self.send_reply(response_types.WAITING_FOR_PLAYER_TO_START_GAME, {
                    'player_name': sender_player[user_model.USER_NAME],
                    'game_id': game_id
                })
            else:
                print("line169")
                self.start_game(game_id)

        return

    def cancel_waiting_for_player(self, gson):
        self.db.remove_waiting_game(gson['game_id'])

    def add_message_in_private_chat(self, gson):
        receiver_player_id = gson['player_id']
        message = gson['message']
        print("method add_message_in_private_chat called")
        self.db.add_message_in_private(self.user[user_model.USER_ID], receiver_player_id, message)

        data = {
            'sender_player_id': self.user[user_model.USER_ID],
            'receiver_player_id': receiver_player_id,
            'message': message,
            'timestamp': utility.get_current_timestamp(),
        }
        self.send_reply(response_types.NEW_PRIVATE_MESSAGE, data)
        connection = get_connection_by_user_id(receiver_player_id)
        if connection is not None:
            connection.send_reply(response_types.NEW_PRIVATE_MESSAGE, data)

    def get_private_chat_messages(self, gson):
        print("method get_private_chat_messages called")
        receiver_player_id = gson['player_id']
        from_message_id = gson['from_message_id']
        if from_message_id == -1:
            chats = self.db.get_last_private_message(self.user[user_model.USER_ID], receiver_player_id)
            must_clear_history = True
        else:
            chats = self.db.get_private_message(self.user[user_model.USER_ID], receiver_player_id, from_message_id)
            must_clear_history = False

        self.send_reply(response_types.PRIVATE_CHAT_MESSAGES, {
            'chat_with': receiver_player_id,
            'messages': chats,
            'must_clear_history': utility.to_json_bool(must_clear_history)
        })

    def get_message(self):
        result = self.db.get_all_message()
        for x in result:
            self.send_message(str(x) + "\n\n")

    def minroob_click_action(self, gson):
        game_id = gson['game_id']
        row = gson['row']
        col = gson['col']
        status, game = self.db.get_minroob_game(game_id)
        clicked_positions = json.loads(game[minroob_model.CLICKED_POSITIONS])
        map = json.loads(game[minroob_model.MAP])
        user_id = self.user[user_model.USER_ID]
        if game[minroob_model.TURN_PLAYER_ID] == user_id:
            if clicked_positions[row][col]:
                self.send_reply(response_types.GAME_MESSAGE, {
                    "message": 'This button has already been selected. Please select another button'
                })
            else:
                if map[row][col] == BOMBS_BUTTON:
                    self.send_reply(response_types.GAME_MESSAGE, {
                        "message": 'Bomb is found! Try another one.'
                    })
                    if game[minroob_model.PLAYER_ONE_ID] == user_id:
                        self.db.increase_player_one_score(game_id)
                    else:
                        self.db.increase_player_two_score(game_id)
                    self.check_game_winner(game_id)
                else:
                    self.db.change_game_turn(game_id)

                clicked_positions[row][col] = True
                self.db.update_clicked_positions(game_id, json.dumps(clicked_positions))
                self.send_game_data(game_id)

        else:
            self.send_reply(response_types.GAME_MESSAGE, {
                'message': 'It\'s not your turn'
            })

    def announcement_of_game(self, gson):
        game_id = gson['game_id']
        status, game = self.db.get_minroob_game(game_id)
        opposing_player_id = self.find_opposing_player_id(game)
        print(str(opposing_player_id))
        self.db.end_game(game_id, opposing_player_id)
        connection = get_connection_by_user_id(opposing_player_id)
        if connection is not None:
            connection.send_reply(response_types.GAME_END, {
                'is_winner': utility.to_json_bool(True),
                'message': 'Your opponent stopped playing with you'
            })

    def get_me(self):
        total_game = self.db.get_total_game_count(self.user[user_model.USER_ID])
        wins = self.db.get_wins_count(self.user[user_model.USER_ID])
        self.send_reply(response_types.ME_DATA, {
            'total_games': total_game,
            'wins': wins,
            'fullname': self.user[user_model.FULLNAME],
            'username': self.user[user_model.USER_NAME],
        })

    def create_game(self, game_id, sender_player_id, receiver_player_id):
        total_bombs = 0
        clicked_positions = [[False] * COL_COUNT] * ROW_COUNT
        row = []
        rdn = random.randrange(0, ROW_COUNT)
        for i in range(0, ROW_COUNT):
            if i == rdn:
                boombs = 3
            else:
                boombs = 2
            total_bombs += boombs
            boombIndexs = []
            for boomb in range(0, boombs):
                boombIndex = random.randrange(0, COL_COUNT)
                while boombIndex in boombIndexs:
                    boombIndex = random.randrange(0, COL_COUNT)

                boombIndexs.append(boombIndex)

            col = []
            for b in range(0, COL_COUNT):
                if b in boombIndexs:
                    col.append(BOMBS_BUTTON)
                else:
                    col.append(EMPTY_BUTTON)

            row.append(col)

        self.db.add_minroob_game(game_id, sender_player_id, receiver_player_id,
                                   total_bombs, json.dumps(row), json.dumps(clicked_positions))
        return row

    def start_game(self, game_id):
        status, game_request = self.db.get_game_request_by_id(game_id)
        sender_player_id = game_request[game_request_model.SENDER_PLAYER_ID]
        receiver_player_id = game_request[game_request_model.RECEIVER_PLAYER_ID]
        sender_connection = get_connection_by_user_id(sender_player_id)
        receiver_connection = get_connection_by_user_id(receiver_player_id)
        if (sender_connection is not None) and (receiver_connection is not None):
            self.db.accept_game_request(game_id)
            status, game = self.db.get_minroob_game(game_id)
            if not status:
                self.create_game(game_id, sender_player_id, receiver_player_id)
            data = {
                'game_id': game_id
            }
            sender_connection.send_reply(response_types.START_GAME, data)
            receiver_connection.send_reply(response_types.START_GAME, data)
            return True

        return False

    def check_game_winner(self, game_id):
        status, game = self.db.get_minroob_game(game_id)
        player_one_score = game[minroob_model.PLAYER_ONE_SCORE]
        player_two_score = game[minroob_model.PLAYER_TWO_SCORE]
        player_one_id = game[minroob_model.PLAYER_ONE_ID]
        player_two_id = game[minroob_model.PLAYER_TWO_ID]
        total_bombs = game[minroob_model.TOTAL_BOMBS]
        winder_id = -1
        available_bombs = total_bombs - player_two_score - player_one_score
        if (player_one_score - player_two_score) > available_bombs:
            winder_id = player_one_id
        if (player_two_score - player_one_score) > available_bombs:
            winder_id = player_two_id
        if winder_id != -1:
            self.db.end_game(game_id, winder_id)
            data_for_winder = {
                "is_winner": utility.to_json_bool(True),
                "message": "You played very well! good job"
            }
            data_for_loser = {
                "is_winner": utility.to_json_bool(False),
                "message": "Try again and hope you win!"
            }
            player_one_connection = get_connection_by_user_id(player_one_id)
            player_two_connection = get_connection_by_user_id(player_two_id)
            if winder_id == player_one_id:
                player_one_connection.send_reply(response_types.GAME_END, data_for_winder)
            else:
                player_one_connection.send_reply(response_types.GAME_END, data_for_loser)

            if winder_id == player_two_id:
                player_two_connection.send_reply(response_types.GAME_END, data_for_winder)
            else:
                player_two_connection.send_reply(response_types.GAME_END, data_for_loser)

    def have_index_bombs(self, map, i, j):
        if i < 0 or i >= ROW_COUNT or j < 0 or j >= COL_COUNT:
            return 0

        try:
            if map[i][j] == BOMBS_BUTTON:
                return 1
            else:
                return 0
        except:
            return 0

    def get_position_simbole(self, map, i, j):
        if map[i][j] == BOMBS_BUTTON:
            return ':bomb:'
        else:
            total_around_bombs = 0
            total_around_bombs += self.have_index_bombs(map, i, (j + 1))
            total_around_bombs += self.have_index_bombs(map, i, (j - 1))
            total_around_bombs += self.have_index_bombs(map, (i - 1), j)
            total_around_bombs += self.have_index_bombs(map, (i - 1), (j + 1))
            total_around_bombs += self.have_index_bombs(map, (i - 1), (j - 1))
            total_around_bombs += self.have_index_bombs(map, (i + 1), j)
            total_around_bombs += self.have_index_bombs(map, (i + 1), (j + 1))
            total_around_bombs += self.have_index_bombs(map, (i + 1), (j - 1))
            return str(total_around_bombs)

    def send_game_data(self, game_id):
        status, game = self.db.get_minroob_game(game_id)
        if not status:
            return

        clicked_positions = json.loads(game[minroob_model.CLICKED_POSITIONS])
        map = json.loads(game[minroob_model.MAP])
        return_map = []
        for i in range(0, ROW_COUNT):
            return_col = []
            for b in range(0, COL_COUNT):
                if clicked_positions[i][b]:
                    return_col.append(self.get_position_simbole(map, i, b))
                else:
                    return_col.append("")

            return_map.append(return_col)

        status, turn_player = self.db.get_player_by_id(game[minroob_model.TURN_PLAYER_ID])
        status, player_one = self.db.get_player_by_id(game[minroob_model.PLAYER_ONE_ID])
        status, player_two = self.db.get_player_by_id(game[minroob_model.PLAYER_TWO_ID])
        status, updated_game = self.db.get_minroob_game(game_id)

        data = {
            "game_id": updated_game[minroob_model.GAME_ID],
            "turn": turn_player[user_model.USER_NAME],
            "player_one": {
                "id": player_one[user_model.USER_ID],
                "name": player_one[user_model.USER_NAME],
                "score": updated_game[minroob_model.PLAYER_ONE_SCORE],
            },
            "player_two": {
                "id": player_two[user_model.USER_ID],
                "name": player_two[user_model.USER_NAME],
                "score": updated_game[minroob_model.PLAYER_TWO_SCORE],
            },
            "data": return_map
        }

        connection1 = get_connection_by_user_id(game[minroob_model.PLAYER_ONE_ID])
        if connection1 is not None:
            connection1.send_reply(response_types.GAME_DATA, data)
        else:
            print("game_data: connection1 is None")

        connection2 = get_connection_by_user_id(game[minroob_model.PLAYER_TWO_ID])
        if connection2 is not None:
            connection2.send_reply(response_types.GAME_DATA, data)
        else:
            print("game_data: connection2 is None")

    def get_game_data(self, gson):
        game_id = gson['game_id']
        status, game = self.db.get_minroob_game(game_id)
        if not status:
            return

        clicked_positions = json.loads(game[minroob_model.CLICKED_POSITIONS])
        map = json.loads(game[minroob_model.MAP])
        return_map = []
        for i in range(0, ROW_COUNT):
            return_col = []
            for b in range(0, COL_COUNT):
                if clicked_positions[i][b]:
                    return_col.append(self.get_position_simbole(map, i, b))
                else:
                    return_col.append("")

            return_map.append(return_col)

        status, turn_player = self.db.get_player_by_id(game[minroob_model.TURN_PLAYER_ID])
        status, player_one = self.db.get_player_by_id(game[minroob_model.PLAYER_ONE_ID])
        status, player_two = self.db.get_player_by_id(game[minroob_model.PLAYER_TWO_ID])
        status, updated_game = self.db.get_minroob_game(game_id)

        data = {
            "game_id": updated_game[minroob_model.GAME_ID],
            "turn": turn_player[user_model.USER_NAME],
            "player_one": {
                "id": player_one[user_model.USER_ID],
                "name": player_one[user_model.USER_NAME],
                "score": updated_game[minroob_model.PLAYER_ONE_SCORE],
            },
            "player_two": {
                "id": player_two[user_model.USER_ID],
                "name": player_two[user_model.USER_NAME],
                "score": updated_game[minroob_model.PLAYER_TWO_SCORE],
            },
            "data": return_map
        }
        self.send_reply(response_types.GAME_DATA, data)


    def get_global_messages(self, gson):
        from_message_id = gson['from_message_id']
        if from_message_id == -1:
            messages = self.db.get_last_global_messages(10)
            must_clear_history = utility.to_json_bool(True)
        else:
            from_message_id = gson['from_message_id']
            messages = self.db.get_global_messages(from_message_id, 10)
            must_clear_history = utility.to_json_bool(False)

        self.send_reply(response_types.GLOBAL_MESSAGES, {
            'messages': messages,
            'must_clear_history': must_clear_history
        })

    def receive_message(self, gson):
        action = gson['action']
        if action == request_types.CREATE_ACCOUNT:
            self.create_account(gson)
        elif action == request_types.AUTH:
            if self.auth is None:
                self.check_auth(gson)
        elif self.auth is None:
            self.send_error(error_types.ERROR_REQUIRE_AUTH, "require_auth")
        elif action == request_types.STOP_SELF:
            self.stop_self()
        elif action == request_types.GET_MESSAGE:
            self.get_message()
        elif action == request_types.ADD_MESSAGE:
            self.add_message(gson)
        elif action == request_types.SEND_BROADCAST:
            broadcast_json(response_types.GAME_END, {
                'is_winner': utility.to_json_bool(True),
                'message': 'You Win!'
            })
        elif action == request_types.GLOBAL_MESSAGE:
            self.add_global_message(gson)
        elif action == request_types.GET_ONLINE_PLAYERS:
            self.get_online_players()
        elif action == request_types.GAME_REQUEST:
            self.game_request(gson)
        elif action == request_types.GET_GAME_REQUESTS:
            self.get_incoming_game_request()
            self.get_outgoing_game_request()
        elif action == request_types.CANCEL_GAME_REQUEST:
            self.cancel_game_request(gson)
        elif action == request_types.ACCEPT_GAME_REQUEST:
            self.accept_game_request(gson)
        elif action == request_types.ADD_MESSAGE_IN_PRIVATE_CHAT:
            self.add_message_in_private_chat(gson)
        elif action == request_types.GET_PRIVATE_CHAT_MESSAGES:
            self.get_private_chat_messages(gson)
        elif action == request_types.CANCEL_WAITING_FOR_PLAYER:
            self.cancel_waiting_for_player(gson)
        elif action == request_types.GET_GAME_DATA:
            self.get_game_data(gson)
        elif action == request_types.MINROOB_CLICK_ACTION:
            self.minroob_click_action(gson)
        elif action == request_types.GET_RUNNING_GAME:
            self.get_running_game()
        elif action == request_types.ANNOUNCEMENT_OF_LOSS_GAME:
            self.announcement_of_game(gson)
        elif action == request_types.GET_GLOBAL_MESSAGES:
            self.get_global_messages(gson)
        elif action == request_types.GET_ME:
            self.get_me()
        elif action == "test_create_game":
            self.create_game()

    def get_data_with_pattern(self):
        data = b''
        while True:
            data += self.socket.recv(RECV_BUFFER)
            print(utility.byte_to_string(data))
            if (re.match("<Ent>.*</Ent>", utility.byte_to_string(data))):
                data = utility.byte_to_string(data).replace("<Ent>", "").replace("</Ent>", "")
                break
        return data

    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

    def run(self):
        while self.signal:
            data = b''
            try:
                data = self.socket.recv(RECV_BUFFER)
            except:
                print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                self.change_player_status(False)
                if self in connections:
                    connections.remove(self)
                break
            finally:
                if data.decode("utf-8") != "":
                    try:
                        array = data.decode("utf-8").split("\r\n")
                        for item in array:
                            if item != '':
                                print("item: " + item)
                                gson = json.loads(item)
                                self.receive_message(gson)

                    except Exception as e:
                        print(traceback.format_exc())


def broadcast_json(type, data, exclude=[]):
    print('broadcast: ' + type + " data: " + str(data))
    broadcast_data(json.dumps({
        'status': 'ok',
        'type': type,
        'data': str(data),
    }), exclude)


def get_connection_by_user_id(user_id):
    for connection in connections:
        # if the socket is not the server or the client from which the message originated
        if connection != server_socket and isinstance(connection, Client):
            if connection.user is not None:
                if connection.user[user_model.USER_ID] == user_id:
                    return connection

    return None


def broadcast_data(message, exclude=[]):
    for connection in connections:
        # if the socket is not the server or the client from which the message originated
        if connection != server_socket:
            try:
                if isinstance(connection, Client):
                    if connection.user[user_model.USER_ID] not in exclude:
                        connection.send_message(message)
                elif isinstance(connection, socket.socket):
                    connection.send("a\n".encode("utf-8"))
                else:
                    print(str(type(connection)))
                    print(str(connection is socket.socket))
            except Exception as a:
                # if the socket connection is broke, close the socket and remove it
                try:
                    print("client is client not send " + str(a))
                    if isinstance(connection, Client):
                        connection.socket.close()
                    elif isinstance(connection, socket.socket):
                        connection.close()
                    connections.remove(socket)
                except:
                    print("problem")


def newConnections(socket):
    while True:
        global connections
        sock, address = socket.accept()
        require_auth_message = json.dumps({
            "status": "error",
            "code": error_types.ERROR_REQUIRE_AUTH,
            "message": 'require_auth'
        })
        sock.send(str("" + require_auth_message + "\r\n").encode('utf8'))
        connections.append(Client(sock, address, True))
        connections[len(connections) - 1].start()
        print("New Connection at ID ")


if __name__ == "__main__":
    # keep list of all sockets
    PORT = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_ip = socket.gethostbyname(HOST)
    print(socket_ip)
    server_socket.bind((socket_ip, PORT))
    server_socket.listen(500)

    print("Server listening on port " + str(PORT))
    global_db = database.Db(username=db_setting['username'], password=db_setting['password'], host=db_setting['host'],
                          dbname=db_setting['dbname'])
    # create while loop for accept connection request
    newConnectionThread = threading.Thread(target=newConnections, args=(server_socket,))
    newConnectionThread.start()
    print(str("💣"))
