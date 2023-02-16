from sqlalchemy.orm.session import Session
from chat.src.schemas.chatroom_schema import EventBase
from chat.src.models.chatroom_model import DbEvent

def add_chatroom(db: Session, request: EventBase):
    new_event = DbEvent(
        title=request.title,
        description=request.description,
        is_public=request.is_public,
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    
    return new_event


def get_chatroom_by_id(db: Session, event_id: int):
    return db.query(DbEvent).filter(DbEvent.id == event_id).first()

def update_chatroom(db: Session, event_id: int, request: DbEvent):
    event = db.query(DbEvent).filter(DbEvent.id == event_id).first()
    if event:
        event.title = request.title
        event.description = request.description
        event.is_public = request.is_public
        
        db.add(event)
        db.commit()
        db.refresh(event)

    return event

def delete_chatroom(db: Session, event_id: int,):
    event = db.query(DbEvent).filter(DbEvent.id == event_id).first()
    if event:
        db.delete(event)
        db.commit()
    return event