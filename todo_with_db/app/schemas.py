from pydantic import BaseModel, Field
from uuid import UUID

#  Define the data structure for creating and reading todos

class TodoBase(BaseModel):
    title: str = Field(...,example="Buy goceries")
    description: str  = Field(..., example="Buy eggs,milk,bread,vegetables from the supermarket")
    completed: bool = Field(False, example=False)

class TodoCreate(TodoBase):
     pass


class TodoResponse(TodoBase):
    id: UUID
    

    class Config:
        orm_mode = True
