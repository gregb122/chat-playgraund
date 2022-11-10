from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user_schema import UserBase, UserDisplay
from helpers.database import get_db

from repository import db_user
from helpers.responses import not_found

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={
        200: {
            "description": "Returns User object"
        }
    }
)

@router.post('/register', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

@router.get('/all', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

@router.get('/{id}', response_model=UserDisplay, 
            responses={404: not_found('User 1 not found')})
def get_user(id: int, db: Session = Depends(get_db)):
    user = db_user.get_user_by_id(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User {id} not found")
    return user

@router.patch('/{id}/update', 
              response_model=UserDisplay, 
              responses={404: not_found('User 1 not found')})
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    user = db_user.update_user(db, id, request)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User {id} not found")
    return user

@router.delete('/{id}/delete', 
               response_model=UserDisplay, 
               responses={404: not_found('User 1 not found')})
def delete(id: int, db: Session = Depends(get_db)):
    user = db_user.delete_user(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User {id} not found")
    return user