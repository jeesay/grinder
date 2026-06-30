import asyncio
import websockets
import os

async def tail_file(websocket, file_path):
    """Wtach new lines append to log.txt and send them."""
    if not os.path.exists(file_path):
        await websocket.send(f"Error : file {file_path} doesn't exist.")
        return

    print(f"Start monitoring of : {file_path}")
    
    with open(file_path, "r") as f:
        
        while True:
            line = f.readline()
            if not line:
                # No new lines, we waiting a bit before re-try
                await asyncio.sleep(0.5)
                continue
            
            # sending new lines to client
            await websocket.send(line.strip())

async def handler(websocket):
    async for message in websocket:
        if message == "start_log":
            print("Commande de log reçue")
            # We launch file reading to background
            asyncio.create_task(tail_file(websocket, "log.txt"))
        else:
            await websocket.send(f"Commande inconnue : {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Serveur de monitoring lancé sur ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())