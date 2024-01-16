
import asyncio
import websockets

async def connect_to_websocket(message, User):
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        message_to_send = message
        await websocket.send(f"{User}: {message_to_send}")
        print(f"{User} Sent to server: {message_to_send}")

        # Receive and print the server's response
        response = await websocket.recv()
        print(f"Received from server: {response}")

# Run the client
async def escutar_mensagens_do_servidor(counter, winObject):
    async with websockets.connect('ws://localhost:8765') as websocket:
        print('okkkk conexão feita')
        while True:
            mensagem = await websocket.recv()
            winObject.addstr(1+counter[0],1,mensagem)
            counter[0] = counter[0]+1
            winObject.refresh()
            print(f"Recebido do servidor: {mensagem}")


def wrapper_escutar_mensagens_do_servidor(url, winObject):
    asyncio.run(escutar_mensagens_do_servidor(url, winObject))
