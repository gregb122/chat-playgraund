from chat.src.inventory_api.repository import db_chatroom
from helpers.database import get_db
from schemas.event_schema import EventBase, EventDisplay
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from chat.src.inventory_api.repository import db_message


router = APIRouter(
    prefix='/{user_id}/plants/{plant_id}/events',
    tags=['event']
)

@router.post('/add', response_model=EventDisplay)
def add_event(request: EventBase, user_id: int, plant_id: int, db: Session = Depends(get_db)):
    plant = db_message.get_plant_by_id(db, plant_id)
    if plant and plant.owner_id == user_id:
        return db_chatroom.add_event(db, plant_id, request)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"plant {plant_id} of user {user_id} not found")

@router.get('/{event_id}', response_model=EventDisplay)
def get_event(user_id: int, plant_id: int, event_id: int, db: Session = Depends(get_db)):
    event =  db_chatroom.get_event_by_id(db, event_id)
    if event and event.plant_id == plant_id and event.plant.owner_id == user_id:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Event {event_id} of plant {plant_id} of user {user_id} not found")

@router.patch('/{event_id}/update',response_model=EventDisplay)
def update_event(request: EventBase, user_id: int, plant_id: int, event_id: int, db: Session = Depends(get_db)):
    event =  db_chatroom.get_event_by_id(db, event_id)
    if event and event.plant_id == plant_id and event.plant.owner_id == user_id:
        return db_chatroom.update_event(db, event_id, request)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Event {event_id} of plant {plant_id} of user {user_id} not found")

@router.delete('/{event_id}/delete', response_model=EventDisplay)
def delete_event(user_id: int, plant_id: int, event_id:int, db: Session = Depends(get_db)):
    event =  db_chatroom.get_event_by_id(db, event_id)
    if event and event.plant_id == plant_id and event.plant.owner_id == user_id:
        return db_chatroom.delete_event(db, event_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Event {event_id} of plant {plant_id} of user {user_id} not found")
