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

# AsyncStreamRead (TCP echo server)
## Start this first then do AsyncStreamWrite
#### https://docs.python.org/3/library/asyncio-stream.html#examples

```python
import asyncio
```

```python
async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
```

```python
async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8889)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

#asyncio.run(main())
await main()
```
