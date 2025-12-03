from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="TODO API",
    version="1.0.0"
)

# In-memory storage for TODO items
todos_db: List[dict] = []
next_id = 1

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos_db

@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = {
        "id": next_id,
        "title": todo.title,
        "completed": todo.completed
    }
    todos_db.append(new_todo)
    next_id += 1
    return new_todo

@app.get("/todos/{id}", response_model=Todo)
def get_todo(id: int):
    for todo in todos_db:
        if todo["id"] == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{id}", status_code=204)
def delete_todo(id: int):
    global todos_db
    initial_length = len(todos_db)
    todos_db = [todo for todo in todos_db if todo["id"] != id]
    if len(todos_db) == initial_length:
        raise HTTPException(status_code=404, detail="Todo not found")
    return
