from fastapi import APIRouter, Depends, HTTPException , status
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.dependencies import get_db
from typing import List

router = APIRouter(
    prefix="/todos",           
    tags=["Todos"]            
)


#  Get all todos
@router.get("/", response_model=List[schemas.TodoResponse], status_code=status.HTTP_200_OK)
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return todos


#  Get a todo by ID
@router.get("/{todo_id}", response_model=schemas.TodoResponse, status_code=status.HTTP_200_OK)
def get_todo(todo_id: str, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


#  Create a new todo
@router.post("/", response_model=schemas.TodoResponse , status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    new_todo = models.Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


#  Update a todo
@router.put("/{todo_id}", response_model=schemas.TodoResponse, status_code=status.HTTP_200_OK)
def update_todo(todo_id: str, updated_todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.completed = updated_todo.completed
    db.commit()
    db.refresh(todo)
    return todo


#  Delete a todo
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
   
