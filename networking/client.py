import asyncio

# When either join game request or update request
async def send_and_receive(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Client sends: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    received_message = data.decode()
    print(f'Client received: {received_message!r}')

    writer.close()
    print('Client closed the connection\n')

    return received_message

# When clicking
async def send_only(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Client sends: {message!r}')
    writer.write(message.encode())
    writer.close()
    print(f'Client closed the connection\n')

asyncio.run(send_and_receive('u'))
