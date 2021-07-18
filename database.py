import time

import mysql.connector
from mysql.connector import errorcode

import constant
import utility


class Db:
    def __init__(self, username, password, host, dbname):
        print("Db class created")
        self.connect(username, password, host, dbname)

    def connect(self, username, password, host, dbname):
        try:
            global cnx
            cnx = mysql.connector.connect(user=username,
                                          password=password,
                                          host=host,
                                          database=dbname)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                cnx.reconnect()
                print("error line30 : "+ str(err))

    def close(self):
        cnx.close()

    def get_cursor(self):
        try:
            return cnx.cursor()
        except:
            cnx.reconnect()
            return self.get_cursor()

    def create_account(self, username, password, fullname, token):
        cur = self.get_cursor()
        sql = "INSERT INTO players " \
              "(`is_online`,`last_update_time`,`name`,`password`,`username`,`socket_token`) " \
              "VALUES " \
              "(false , %s, %s , %s , %s , %s)"
        cur.execute(sql, (utility.get_current_timestamp(), fullname, password, username, token))
        cnx.commit()

    def get_all_message(self):
        cur = self.get_cursor()
        cur.execute("SELECT * FROM testmessage INNER JOIN users ON testmessage.user_id=users.id")
        myresult = cur.fetchall()
        cnx.commit()
        return myresult

    def get_player_by_token(self, token):
        cur = self.get_cursor()
        sql = "SELECT * FROM players WHERE socket_token=%s;"
        cur.execute(sql, (token,))
        result = cur.fetchall()
        cnx.commit()
        if len(result) == 1:
            return True, result[0]
        else:
            return False, None

    def get_player_by_userpass(self, username, password):
        cur = self.get_cursor()
        sql = "SELECT * FROM players WHERE username=%s AND password=%s;"
        cur.execute(sql, (username, password,))
        result = cur.fetchall()
        if len(result) == 1:
            return True, result[0]
        else:
            return False, None

    def get_online_players(self, own_player_id):
        cur = self.get_cursor()
        sql = "SELECT username,name,id FROM players WHERE is_online=true AND id != %s;"
        cur.execute(sql, (own_player_id,))
        result = cur.fetchall()
        cnx.commit()
        response = []
        for player in result:
            response.append({
                'fullname': player[1],
                'username': player[0],
                'id': player[2],
            })
        return response

    def add_global_message(self, player_id, message):
        cur = self.get_cursor()
        sql = "INSERT INTO global_chat (`player_id`,`message`,`timestamp`)VALUES(%s,%s,%s)"
        value = (player_id, message, utility.get_current_timestamp())
        cur.execute(sql, value)
        cnx.commit()

    def set_player_status(self, player_id, status):
        print("change player status")
        cur = self.get_cursor()
        sql = "UPDATE players SET is_online=%s WHERE id=%s;"
        value = (status, player_id)
        cur.execute(sql, value)
        cnx.commit()

    def get_player_by_id(self, id):
        cur = self.get_cursor()
        sql = "SELECT * FROM players WHERE id=%s"
        cur.execute(sql, (id,))
        result = cur.fetchall()
        cnx.commit()
        if len(result) == 1:
            return True, result[0]
        else:
            return False, None

    def add_message(self, userid, message):
        cur = self.get_cursor()
        sql = "INSERT INTO testmessage (`user_id`,`message`)VALUES(%s,%s)"
        value = (userid, message)
        cur.execute(sql, value)
        cnx.commit()

    def remove_game_request(self, sender_player_id, receiver_player_id):
        cur = self.get_cursor()
        sql = "DELETE FROM game_requests WHERE `sender_player_id`=%s AND `receiver_player_id`=%s;"
        value = (sender_player_id, receiver_player_id,)
        cur.execute(sql, value)
        cnx.commit()

    def add_game_request(self, sender_player_id, receiver_player_id):
        cur = self.get_cursor()
        sql = "INSERT INTO game_requests (`sender_player_id`,`receiver_player_id`,`timestamp`) VALUES (%s,%s,%s)"
        value = (sender_player_id, receiver_player_id, utility.get_current_timestamp())
        cur.execute(sql, value)
        cnx.commit()

    def get_incoming_game_request(self, player_id):
        cur = self.get_cursor()
        sql = "SELECT players.username, players.name,players.id, game_requests.id,game_requests.timestamp FROM game_requests INNER JOIN players ON players.id = game_requests.sender_player_id WHERE receiver_player_id=%s AND is_accepted=0;"
        cur.execute(sql, (player_id,))
        result = cur.fetchall()
        cnx.commit()
        response = []
        for game_request in result:
            response.append({
                'fullname': game_request[1],
                'username': game_request[0],
                'id': game_request[3],
                'player_id': game_request[2],
                'timestamp': game_request[4],
            })
        return response

    def get_outgoing_game_request(self, player_id):
        cur = self.get_cursor()
        sql = "SELECT players.username, players.name,players.id, game_requests.id,game_requests.timestamp FROM game_requests INNER JOIN players ON players.id = game_requests.receiver_player_id WHERE sender_player_id=%s AND is_accepted=0;"
        cur.execute(sql, (player_id, ))
        result = cur.fetchall()
        cnx.commit()
        response = []
        for game_request in result:
            response.append({
                'fullname': game_request[1],
                'username': game_request[0],
                'id': game_request[3],
                'player_id': game_request[2],
                'timestamp': game_request[4],
            })
        return response

    def accept_game_request(self, game_id):
        cur = self.get_cursor()
        sql = "UPDATE game_requests SET is_accepted=true WHERE id = %s;";
        cur.execute(sql, (game_id, ))
        cnx.commit()

    def cancel_game_request(self, game_id):
        cur = self.get_cursor()
        sql = "DELETE FROM game_requests WHERE id=%s;"
        cur.execute(sql, (game_id,))
        cnx.commit()

    def get_receiver_play_id_by_game_id(self, game_id):
        cur = self.get_cursor()
        sql = "SELECT game_requests.receiver_player_id FROM game_requests WHERE id=%s;"
        cur.execute(sql, (game_id,))
        result = cur.fetchall()
        cnx.commit()
        if len(result) == 1:
            return True, result[0][0]
        else:
            return False, None

    def add_message_in_private(self, sender_player_id, receiver_player_id, message):
        cur = self.get_cursor()
        sql = "INSERT INTO `private_chats` (`sender_player_id`, `receiver_player_id`, `message`, `timestamp`) VALUES (%s,%s,%s,%s);"
        value = (sender_player_id, receiver_player_id, message, utility.get_current_timestamp())
        cur.execute(sql, value)
        cnx.commit()

    def get_last_private_message(self, player1_id, player2_id, limit=10):
        cur = self.get_cursor()
        sql = "SELECT * FROM `private_chats` WHERE ((sender_player_id=%s AND receiver_player_id=%s) OR (receiver_player_id=%s AND sender_player_id=%s)) ORDER BY id DESC LIMIT %s;"
        cur.execute(sql, (player1_id, player2_id, player1_id, player2_id, limit))
        result = cur.fetchall()
        cnx.commit()
        response = []
        for item in result:
            response.append({
                'id':item[0],
                'sender_pla0yer_id': item[1],
                'receiver_player_id': item[2],
                'message': item[3],
                'timestamp': item[4],
            })

        response.reverse()
        return response

    def get_private_message(self, player1_id, player2_id, from_message_id, limit=10):
        cur = self.get_cursor()
        sql = "SELECT * FROM `private_chats` WHERE " \
              "(((sender_player_id=%s AND receiver_player_id=%s)" \
              " OR (receiver_player_id=%s AND sender_player_id=%s))) " \
              " AND id < %s ORDER BY id DESC LIMIT %s;"
        cur.execute(sql, (player1_id, player2_id, player1_id, player2_id, from_message_id, limit))
        result = cur.fetchall()
        cnx.commit()
        response = []
        for item in result:
            response.append({
                'id': item[0],
                'sender_player_id': item[1],
                'receiver_player_id': item[2],
                'message': item[3],
                'timestamp': item[4],
            })

        response.reverse()
        return response

    def get_game_request_by_id(self, game_id):
        cur = self.get_cursor()
        sql = "SELECT * FROM `game_requests` WHERE id=%s;"
        cur.execute(sql, (game_id, ))
        result = cur.fetchall()
        cnx.commit()
        if len(result) == 1:
            return True, result[0]
        else:
            return False, None

    def add_waiting_game(self, game_id):
        cur = self.get_cursor()
        sql = "INSERT INTO `waiting_games` (`game_id`, `timestamp`) VALUES (%s,%s);"
        cur.execute(sql, (game_id, utility.get_current_timestamp(), ))
        cnx.commit()

    def remove_waiting_game(self, game_id):
        cur = self.get_cursor()
        sql = "DELETE FROM `waiting_games` WHERE `game_id`=%s;"
        cur.execute(sql, (game_id, ))
        cnx.commit()

    def add_minroob_game(self, game_id, player_one_id, player_two_id, total_bombs, map, clicked_positions):
        cur = self.get_cursor()
        sql = "INSERT INTO `minroob_game`" \
              " (`game_id`, `map`, `turn_player_id`, `player_one_id`," \
              " `player_two_id`, `total_bombs`, `clicked_positions`)" \
              " VALUES " \
              "(%s , %s , %s , %s , %s, %s,%s);"
        cur.execute(sql, (game_id, map, player_one_id, player_one_id,
                          player_two_id, total_bombs, clicked_positions))
        cnx.commit()

    def get_minroob_game(self, game_id):
        cur = self.get_cursor()
        sql = "SELECT * FROM `minroob_game` WHERE `game_id`=%s;"
        cur.execute(sql, (game_id,))
        result = cur.fetchall()
        cnx.commit()
        if len(result) >= 1:
            return True, result[0]
        else:
            return False, None

    def increase_player_one_score(self, game_id):
        cur = self.get_cursor()
        sql = "UPDATE `minroob_game` SET `player_one_score` = `player_one_score` + 1 WHERE `game_id`=%s;"
        cur.execute(sql, (game_id,))
        cnx.commit()

    def increase_player_two_score(self, game_id):
        cur = self.get_cursor()
        sql = "UPDATE `minroob_game` SET `player_two_score` = `player_two_score` + 1 WHERE `game_id`=%s;"
        cur.execute(sql, (game_id,))
        cnx.commit()

    def update_clicked_positions(self, game_id, clicked_positions):
        cur = self.get_cursor()
        sql = "UPDATE `minroob_game` SET `clicked_positions` = %s WHERE `game_id`=%s;"
        cur.execute(sql, (clicked_positions,game_id,))
        cnx.commit()

    def change_game_turn_to_id(self, game_id, player_id):
        cur = self.get_cursor()
        sql = "UPDATE `minroob_game` SET `turn_player_id` = %s WHERE `game_id`=%s;"
        cur.execute(sql, (player_id, game_id,))
        cnx.commit()

    def change_game_turn(self, game_id):
        cur = self.get_cursor()
        sql = "SELECT `player_one_id`,`player_two_id`,`turn_player_id` FROM `minroob_game` WHERE `game_id`=%s;"
        cur.execute(sql, (game_id,))
        result = cur.fetchall()
        cnx.commit()
        player_one_id = result[0][0]
        player_two_id = result[0][1]
        turn = result[0][2]

        if turn == player_one_id:
            self.change_game_turn_to_id(game_id, player_two_id)
        else:
            self.change_game_turn_to_id(game_id, player_one_id)

    def get_waiting_game_request(self, player_id):
        cur = self.get_cursor()
        sql = "SELECT game_requests.* FROM `waiting_games` INNER JOIN game_requests WHERE game_requests.sender_player_id = %s"
        cur.execute(sql, (player_id,))
        result = cur.fetchall()
        cnx.commit()
        if len(result) >= 1:
            return result[0]
        else:
            return None

    def end_game(self, game_id, player_id):
        cur = self.get_cursor()
        sql = "UPDATE `minroob_game` SET `winer_id`=%s , `is_finished`=true WHERE `game_id`=%s;"
        cur.execute(sql, (player_id, game_id))
        cnx.commit()
        self.cancel_game_request(game_id)

    def get_running_game(self, player_id):
        cur = self.get_cursor()
        sql = "SELECT * FROM `minroob_game` WHERE is_finished=false AND (player_one_id=%s OR player_two_id=%s);"
        cur.execute(sql, (player_id, player_id, ))
        result = cur.fetchall()
        cnx.commit()
        if len(result) >= 1:
            return result[0]
        else:
            return None

    def get_total_game_count(self, player_id):
        cur = self.get_cursor()
        sql = "SELECT COUNT(id) FROM `minroob_game` WHERE (player_one_id=%s OR player_two_id=%s)"
        cur.execute(sql, (player_id, player_id, ))
        result = cur.fetchall()
        cnx.commit()
        return result[0][0]

    def get_wins_count(self, player_id):
        cur = self.get_cursor()
        sql = "SELECT COUNT(id) FROM `minroob_game` WHERE winer_id=%s;"
        cur.execute(sql, (player_id, ))
        result = cur.fetchall()
        cnx.commit()
        return result[0][0]

    def get_last_global_messages(self, limit=20):
        cur = self.get_cursor()
        sql = "SELECT global_chat.*, players.name FROM `global_chat` " \
              "INNER JOIN players ON players.id = global_chat.player_id " \
              "ORDER BY global_chat.id DESC LIMIT %s;"
        cur.execute(sql, (limit,))
        result = cur.fetchall()
        cnx.commit()
        response = []
        result.reverse()
        for item in result:
            response.append({
                'id': item[0],
                'player_id': item[1],
                'message': item[2],
                'timestamp': item[3],
                'fullname': item[4],
            })
        return response

    def get_global_messages(self, from_message_id, limit=20):
        cur = self.get_cursor()
        sql = "SELECT global_chat.*, players.name FROM `global_chat`" \
              " INNER JOIN players ON players.id = global_chat.player_id" \
              " WHERE global_chat.id < %s ORDER BY global_chat.id DESC LIMIT %s;"
        cur.execute(sql, (from_message_id, limit, ))
        result = cur.fetchall()
        cnx.commit()
        response = []
        result.reverse()
        for item in result:
            response.append({
                'id': item[0],
                'player_id': item[1],
                'message': item[2],
                'timestamp': item[3],
                'fullname': item[4],
            })
        return response