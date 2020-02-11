import asyncio

MAX_CHARACTERS = 100000

# When either join game request or update request
async def send_and_receive(address_port_tuple, client_name: str, message: str):
    reader, writer = await asyncio.open_connection(address_port_tuple[0], address_port_tuple[1])

    send_message = client_name + '|' + message

    print(f'Client sends: {send_message!r}')
    writer.write(send_message.encode())

    data = await reader.read(MAX_CHARACTERS)
    received_message = data.decode()

    print(f'Client received: {received_message!r}')

    received_messages = received_message.split('m')

    received_messages.append(received_message)

    try:
        if received_messages[-2] == "":
            received_messages = received_messages[:-2]
    except IndexError:
        pass

    writer.close()
    print('Client closed the connection\n')

    return received_messages


# When clicking
async def send_only(address_port_tuple, client_name: str, message: str):
    reader, writer = await asyncio.open_connection(address_port_tuple[0], address_port_tuple[1])

    send_message = client_name + '|' + message

    print(f'Client sends: {send_message!r}')
    writer.write(send_message.encode())

    writer.close()
    print(f'Client closed the connection\n')


if __name__ == '__main__':
    pass

    address_port_tuple = '127.0.0.1', 8895
    nickname = "diana"

    # asyncio.run(send_and_receive(address_port_tuple, nickname, 'j'))
    # asyncio.run(send_only(address_port_tuple, nickname, '1_0_123'))
    received_messages = asyncio.run(send_and_receive(address_port_tuple, nickname, 'u'))

    print(received_messages)