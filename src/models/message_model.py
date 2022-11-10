from sqlalchemy.sql.sqltypes import Integer, String, Date
from sqlalchemy.orm import relationship
from helpers.database import Base
from sqlalchemy import Boolean, Column, ForeignKey


class DbPlant(Base):
    __tablename__='plants'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    date = Column(Date)
    owner_id = Column(Integer, ForeignKey('users.id'))
    chatroom_id = Column(Integer, ForeignKey('chatrooms.id'))

    owner = relationship('DbUser', back_populates='plants')
    events = relationship('DbEvent', back_populates='plant')
