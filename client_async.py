import asyncio
import time

import socketio


async def connect(i):
    try:
        sio = socketio.AsyncClient()

        @sio.on('onMessageReceived')
        def on_message(data):
            pass
            # print('data', data)

        print(f"Connecting {i}")
        await sio.connect('http://localhost:80', auth={"userId": "user1"}, wait_timeout=20)

        await asyncio.sleep(5)

        print(f"Sending messages {i}")
        for i in range(1000):
            await sio.emit('sendMessage', {"message": "my message", "channel": "channel1"})

        #print("Disconnecting")
        #await sio.disconnect()
    except Exception as e:
        print("error", e)



async def async_connect():
    tasks = []
    for i in range (1000):
        tasks.append(asyncio.create_task(connect(i)))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = time.time_ns()
    asyncio.run(async_connect())
    end = time.time_ns()
    print(f"took ms", (end - start) // 1_000_000)



