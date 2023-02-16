from typing import List
from pydantic import BaseModel

# ---------- request data ----------
class EventBase(BaseModel):
    title: str
    description: str
    is_public: bool


# ---------- resoponse view ----------
class Plant(BaseModel):
    id: int
    name: str
    class Config():
        orm_mode = True


class EventDisplay(BaseModel):
    title: str
    description: str
    plant: Plant
    class Config():
        orm_mode = True
