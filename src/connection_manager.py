from fastapi import WebSocket
from chat_room import ChatRoom

class ConnectionManager:

    def __init__(self):
        self.connections: dict[int, ChatRoom] = {}

    def get_members(self, room_number: int):
        chat_room: ChatRoom = self.connections.get(room_number)
        if chat_room == None:
            raise ValueError(f"Chat room with number {room_number} doesn't exist")
        return chat_room.members

    async def create_and_connect_room(self, websocket: WebSocket, room_number: int):
        await websocket.accept()
        if self.connections.get(room_number) != None:
            raise ValueError(f"Chat room already exists")
        self.connections[room_number] = ChatRoom(websocket, room_number)
        print(f"Chat room created: {self.connections[room_number]}")

    def remove(self, websocket: WebSocket, room_number: int):
        websocket.close() # HELP
        room: ChatRoom = self.connections.pop(room_number, None)
        if room == None:
            raise ValueError(f"Chat room with number {room_number} doesn't exist")
        print(f"Chat room removed: {room},\nRemaining: {len(self.connections)}")

    async def _notify(self, message: str, room_name: str):
        active_rooms = []
        while len(self.connections[room_name]) > 0:

            websocket = self.connections[room_name].pop()
            await websocket.send_text(message)
            living_connections.append(websocket)
        self.connections[room_name] = living_connections
