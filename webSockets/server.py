#must be running on another prompt

import asyncio
import websockets
lista_users  = []
async def handle_websocket(websocket,  path):

    # Handle incoming messages here
    print(f"new connection baby {websocket}")
    lista_users.append(websocket)
    while True:
        try:
            print(lista_users)
            
            message = await websocket.recv()
            print(f"Received message: {message}")

            # You can add your custom logic here to process the received message

            # Send a response back to the client
            response = f"Server received: {message}"

            for x in lista_users:
                try:
                    await x.send(response)
                except: 
                    pass

        except websockets.exceptions.ConnectionClosed:
            print("WebSocket connection closed")
            
            break

# Start the WebSocket server
start_server = websockets.serve(handle_websocket, "localhost", 8765)

print("WebSocket server started. Listening on ws://localhost:8765")

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()