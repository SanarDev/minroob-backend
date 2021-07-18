from datetime import datetime
import time

def get_time():
    now = datetime.now()
    return now.strftime("%H:%M")


def get_current_timestamp():
    return round(time.time())


def byte_to_string(data):
    return str(data.decode("utf-8")).strip()


def to_json_bool(value):
    if value == True:
        return 1
    else:
        return 0