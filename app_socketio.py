from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import Blueprint, jsonify, request, session
import time

app = Flask(__name__, static_url_path='/static',)
socketio = SocketIO(app, message_queue='redis://redis:6379')

CHANNELS = [f"channel{i}" for i in range(1000)]

USERS = [f"user{i}" for i in range(1000)]

MEMBERS = [f"member{i}" for i in range(1000)]


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        func(*args, **kwargs)
        end = time.time_ns()
        print(f"event {func.__name__} processes in ms", (end - start) // 1_000_000)
    return wrapper

@socketio.on('connect')
@timed
def on_connect():
    userId = request.headers.get("Authorization", None)
    for channel in CHANNELS:
        join_room(channel)

    for user in USERS:
        join_room(user)

    for member in MEMBERS:
        join_room(member)

    emit('onUserUpdated', {"userId": userId, "online": True}, room=userId)

@socketio.on('disconnect')
@timed
def on_disconnect():
    userId = request.headers.get("Authorization", None)
    emit('onUserUpdated', {"userId": userId, "online": False}, room=userId)



@socketio.on('sendMessage')
@timed
def send_message(data):
    emit('onMessageReceived', data, room=data["channel"])


@socketio.on('subscribeChannels')
@timed
def subscribe_channels(channels):
    start = time.time_ns()

    for channel in CHANNELS:
        if channel in channels["channels"]:
            print("joining room", channel)
            join_room(channel)
        else:
            leave_room(channel)

    end = time.time_ns()
    print("subscribed to channels", channels["channels"], (end - start) // 1_000_000)


@app.route('/')
def index():
    return 'Index Page'