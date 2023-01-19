from flask import jsonify
from datetime import datetime as dt

def ping(username: str, suffix: str=None):
    resp = {"who": username, "at": dt.now().strftime("%Y-%m-%d, %H:%M:%S"), "suffix": suffix}

    pong = jsonify(resp)
    pong.status_code = 200

    return pong