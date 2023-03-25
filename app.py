from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__, static_url_path='/static',)
socketio = SocketIO(app)

CHANNELS = ["channel1", "channel2", "channel3"]


@socketio.on('connect')
def test_connect(auth):
    join_room("channel1")
    join_room("channel2")
    join_room("channel3")


@socketio.on('sendMessage')
def send_message(data):
    emit('onMessageReceived', data, room=data["channel"])


@socketio.on('subscribeChannels')
def subscribe_channels(channels):
    print("channels", channels["channels"])
    for channel in CHANNELS:
        if channel in channels["channels"]:
            print("joining room", channel)
            join_room(channel)
        else:
            leave_room(channel)


@app.route('/')
def index():
    return 'Index Page'