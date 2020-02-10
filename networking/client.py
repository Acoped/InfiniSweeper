import asyncio


async def send_and_recieve(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8890)

    print(f'Client sends: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    received_message = data.decode()
    print(f'Client received: {received_message!r}')

    writer.close()
    print('Client closed the connection')

    return received_message

asyncio.run(send_and_recieve('Hello World!'))
