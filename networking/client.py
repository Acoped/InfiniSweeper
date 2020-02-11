import asyncio

MAX_CHARACTERS = 100000

# When either join game request or update request
async def send_and_receive(address_port_tuple, client_name: str, message: str):
    reader, writer = await asyncio.open_connection(address_port_tuple[0], address_port_tuple[1])

    send_message = client_name + '|' + message

    print(f'Client sends: {send_message!r}')
    writer.write(send_message.encode())

    more_packets = "m"
    received_messages = []
    while more_packets == "m":
        data = await reader.read(MAX_CHARACTERS)
        received_message = data.decode()
        more_packets = received_message[-1]
        if more_packets == "m":
            received_message = received_message[:-1]
            print("More packets: Yes")
        else:
            print("More packets: No")
        print(f'Client received: {received_message!r}')
        received_messages.append(received_message)

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
    # pass
    """
    address_port_tuple = '127.0.0.1', 8891
    asyncio.run(send_and_receive(address_port_tuple, 'andreas', 'j'))
    asyncio.run(send_only(address_port_tuple, 'diana', '1_0_123'))
    """
