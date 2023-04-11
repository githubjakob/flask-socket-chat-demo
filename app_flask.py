import time

from flask import Flask, jsonify, request
from flask_socketio import SocketIO


app = Flask(__name__, static_url_path='/static',)

socketio = SocketIO(message_queue='redis://redis:6379')


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        resp = func(*args, **kwargs)
        end = time.time_ns()
        print(f"event {func.__name__} processes in ms", (end - start) // 1_000_000)
        return resp
    return wrapper


@app.route('/')
def index():
    return jsonify(success=True)


@app.route('/channel/<channel_id>/message', methods=['POST'])
@timed
def send_message(channel_id):
    print("#####")
    data = request.get_json()
    socketio.emit('onMessageReceived', data, room=channel_id)
    return jsonify(success=True)
