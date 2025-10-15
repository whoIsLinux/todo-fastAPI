from fastapi import FastAPI
from app.routers import todos
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# include the router here
app.include_router(todos.router)
