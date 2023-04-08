from flask import Flask, jsonify, request
from flask_socketio import SocketIO


app = Flask(__name__, static_url_path='/static',)

socketio = SocketIO(message_queue='redis://redis:6379')


@app.route('/')
def index():
    return jsonify(success=True)


@app.route('/message', methods=['POST'])
def send_message():
    data = request.get_json()
    socketio.emit('onMessageReceived', data, room="channel1")
    return jsonify(success=True)
