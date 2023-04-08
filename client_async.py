import asyncio
from random import randrange

import socketio


async def connect():
    sio = socketio.AsyncClient()

    @sio.on('onMessageReceived')
    def on_message(data):
        pass
        # print('data', data)

    await sio.connect('http://localhost:8000', auth={"userId": "user1"})

    for i in range(100):
        await sio.emit('sendMessage', {"message": "my message", "channel": "channel1"})


async def async_connect():
    for i in range (1000):
        task = asyncio.create_task(
            connect()
        )
        await task

if __name__ == '__main__':
    asyncio.run(async_connect())



