from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from typing import Annotated
import models 
from database import engine, SessionLocal
from models import Todos
from pydantic import BaseModel, Field
from routers import auth, todos, admin, users


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get('/healthy')
def health_check():
    return {'message': 'Hello World'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)





