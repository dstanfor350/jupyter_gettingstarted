---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# AsyncStreamWriter
## Start AsyncStreamRead first, then this AsyncStreamWriter
#### https://docs.python.org/3/library/asyncio-stream.html#examples

```python
import asyncio
```

```python
async def tcp_echo_client(message):
    connect = asyncio.open_connection('127.0.0.1', 8889)
    reader, writer = await connect
    
    print(f'Encoded: {message!r}')
    writer.write(message.encode())
    await writer.drain()
    
    print('read from reader')
    data = await reader.read(100)
    
    print(f'Received: {data.decode()!r}')
    
    print('Close the connection')
    writer.close()
    await writer.wait_closed()         
```

```python
#asyncio.run(tcp_echo_client('Hellw World!'))
await tcp_echo_client('Hellw World!')
```
