from fastapi import WebSocket
import datetime


class ChatRoom:
    def __init__(self, _web_socket: WebSocket, _room_number: int, _room_name: str="", _description: str=""):
        self.room_number: int = _room_number
        self.room_name: str = _room_name
        self.description: str = _description
        self.members: list[str] = []
        self.messages: list[str, str, datetime.datetime] = []
        
        self.web_socket: WebSocket = _web_socket #without it becouse we can't picle this
