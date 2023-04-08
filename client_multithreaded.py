import concurrent

import socketio


def connect():
    sio = socketio.Client()

    @sio.on('onMessageReceived')
    def on_message(data):
        pass

    sio.connect('http://localhost:8000', auth={"userId": "user1"})
    for i in range(10):
        sio.emit('sendMessage', {"message": "my message", "channel": "channel1"})

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(100):
            futures.append(executor.submit(connect))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()