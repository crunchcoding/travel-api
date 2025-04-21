from sqlalchemy import Column, Integer, String
from app.database import Base

class Destination(Base):
    __tablename__ = "destinations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    description = Column(String)
    best_time = Column(String)
