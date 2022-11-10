from sqlalchemy.orm.session import Session

from helpers.exceptions import AdminUserameException
from helpers.hash import Hash
from schemas.user_schema import UserBase
from models.user_model import DbUser

def create_user(db: Session, request: UserBase):
    if 'admin' in request.username.lower():
        raise AdminUserameException()
    
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user_by_id(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if user:
        user.username = request.username
        user.email = request.email
        user.password = Hash.bcrypt(request.password)
        
        db.add(user)
        db.commit()
        db.refresh(user)

    return user
        
def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if user:
        db.delete(user)
        db.commit()
    return user