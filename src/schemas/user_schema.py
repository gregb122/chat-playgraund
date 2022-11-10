from typing import List
from pydantic import BaseModel


# ---------- request data ----------
class UserBase(BaseModel):
    username: str
    email: str
    password: str


# ---------- resoponse view ----------
class Plant(BaseModel):
    id: int
    name: str
    class Config():
        orm_mode = True
        
        
class UserDisplay(BaseModel):
    username: str
    email: str
    plants: List[Plant] = []
    class Config():
        orm_mode = True
