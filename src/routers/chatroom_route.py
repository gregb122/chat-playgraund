from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from chat.src.inventory_api.repository import db_message
from helpers.database import get_db
from chat.src.schemas.message_schema import PlantBase, PlantDisplay

from repository import db_user


router = APIRouter(
    prefix='/{user_id}/plants',
    tags=['plants'],
)

@router.post('/add', response_model=PlantDisplay)
def add_plant(request: PlantBase, user_id: int, db: Session = Depends(get_db)):
    user = db_user.get_user_by_id(db, user_id)
    if user.id == user_id:
        return db_message.add_plant(db, user_id, request)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User {user_id} not found")

@router.get('/{plant_id}', response_model=PlantDisplay)
def get_plant(user_id: int, plant_id: int, db: Session = Depends(get_db)):
    plant =  db_message.get_plant_by_id(db, plant_id)
    if plant.owner_id == user_id:
        return plant
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"plant {plant_id} of user {user_id} not found")

@router.patch('/{plant_id}/update',response_model=PlantDisplay)
def update_plant(request: PlantBase, user_id: int, plant_id: int, db: Session = Depends(get_db)):
    plant =  db_message.get_plant_by_id(db, plant_id)
    if plant.owner_id == user_id:
        return db_message.update_plant(db, plant_id, request)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"plant {plant_id} of user {user_id} not found")

@router.delete('/{plant_id}/delete', response_model=PlantDisplay)
def delete_plant(user_id: int, plant_id: int, db: Session = Depends(get_db)):
    plant =  db_message.get_plant_by_id(db, plant_id)
    if plant.owner_id == user_id:
        return db_message.delete_plant(db, plant_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"plant {plant_id} of user {user_id} not found")
