from typing import List
from pydantic import BaseModel


# ---------- request data ----------
class PlantBase(BaseModel):
    name: str
    description: str
    is_public: bool


# ---------- resoponse view ----------
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True

 
class Event(BaseModel):
    id: int
    title: str
    class Config():
        orm_mode = True

    
class PlantDisplay(BaseModel):
    name: str
    description: str
    owner: User
    events: List[Event] = []
    class Config():
        orm_mode = True

