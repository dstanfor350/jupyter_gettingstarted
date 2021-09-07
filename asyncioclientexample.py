import asyncio

async def tcp_echo_client(message):
    print(f'Echo message: {message}')
    #reader, writer = await asyncio.open_connection('127.0.0.1', 8889)
    connect = asyncio.open_connection('127.0.0.1', 8889)
    reader, writer = await connect
    
    print(f'Encoded message {message}')
    writer.write(message.encode())
    await writer.drain()
    
    print('read from reader')
    data = await reader.read(100)
    
    print(f'Received: {data.decode()!r}')
    
    print('Close the connection')
    writer.close()
    await writer.wait_closed()

#asyncio.run(tcp_echo_client('Hello World!'))
await tcp_echo_client('Hello World!')


