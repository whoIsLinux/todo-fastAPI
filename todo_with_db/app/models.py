from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base 
import uuid


class Todo(Base):
    __tablename__ = "todos"  

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  
    title = Column(String(255), nullable=False)        
    description = Column(String(255), nullable=True)   
    completed = Column(Boolean, default=False, nullable=False)  
