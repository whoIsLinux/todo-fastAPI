from pydantic import BaseModel

#  Define the data structure for creating and reading todos

class TodoBase(BaseModel):
    title: str
    description: str  = None
    completed: bool = False

class TodoCreate(TodoBase):
     pass



class TodoResponse(TodoBase):
    id: int
    

    class Config:
        orm_mode = True
