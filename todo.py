from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List



#define the model
class Todo(BaseModel):
    title:str
    description:str
    completed:bool=False

app =FastAPI()

todos=[]

    #post endpoint to add a new todo
@app.post("/todo")
async def add_todo(todo:Todo):
    new_id = 10000 + len(todos) + 1

    todo_dict = {'id':new_id , **todo.dict()}

    todos.append(todo_dict)
    return todo_dict
    

 # get all todos
@app.get("/todos")
async def get_todos():
    return todos


 #get a single todo by id
@app.get("/todo/{todo_id}" , response_model=dict)
async def get_todo(todo_id:int):
    for todo in todos:
        if todo['id']==todo_id:
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')    


# update a todo by id
@app.put("/todo/{todo_id}", response_model=dict)
async def update_todo(todo_id:int , updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo['id']==todo_id:
            todos[index].update(updated_todo.dict())
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

#delete a todo by id
@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            deleted_todo=todos.pop(index)
            return {"message": "Todo deleted successfully", "deleted_todo": deleted_todo}
    raise HTTPException(status_code=404, detail="Todo not found")

 