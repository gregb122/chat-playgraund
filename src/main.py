import datetime
import uvicorn


from fastapi import FastAPI, Request, Response, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

#TODO: Use redis to store curent rooms, meseges and connected users
class ChatRoom:
    def __init__(self, _web_socket: WebSocket, _room_number: int, _room_name: str, _description: str):
        self.room_number: int = _room_number
        self.room_name: str = _room_name
        self.description: str = _description
        self.web_socket: WebSocket = _web_socket #withat it becouse we can't picle this
        self.conected_users: list[str] = []
        self.messages: list[str, str, datetime.datetime] = []
    


# manager, for now only 1 chat room is avaible (WIP)
class SocketManager:
    def __init__(self):
        self.active_connections: list[(WebSocket, str)] = []

    async def connect(self, websocket: WebSocket, user: str):
        await websocket.accept()
        self.active_connections.append((websocket, user))

    def disconnect(self, websocket: WebSocket, user: str):
        self.active_connections.remove((websocket, user))

    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection[0].send_json(data)   

manager = SocketManager()
app = FastAPI()
templates = Jinja2Templates(directory="/home/gbiel/chat_api/chat/templates")



@app.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/chat")
def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.get("/api/current_user")
def get_user(request: Request):
    return request.cookies.get("X-Authorization")

class RegisterValidator(BaseModel):
    username: str
    class Config:
        orm_mode = True

@app.post("/api/register")
def register_user(user: RegisterValidator, response: Response):
    response.set_cookie(key="X-Authorization", value=user.username, httponly=True)    

@app.websocket("/api/chat")
async def chat(websocket: WebSocket):
    sender = websocket.cookies.get("X-Authorization")
    if sender:
        await manager.connect(websocket, sender)
        response = {
            "sender": sender,
            "message": "got connected"
        }
        await manager.broadcast(response)
        try:
            while True:
                data = await websocket.receive_json()
                await manager.broadcast(data)
        except WebSocketDisconnect:
            manager.disconnect(websocket, sender)
            response['message'] = "left the chat"
            await manager.broadcast(response)
            

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)