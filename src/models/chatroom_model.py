from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from helpers.database import Base
from sqlalchemy import Column


class DbEvent(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    is_public = Column(Boolean)

