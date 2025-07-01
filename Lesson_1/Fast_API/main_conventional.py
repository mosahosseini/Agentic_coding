from fastapi import FastAPI , HTTPException
from typing import List , Optional
from pydantic import BaseModel , Field
from enum import IntEnum
app = FastAPI()

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class TodoBase(BaseModel):
    todo_name:str = Field(... , min_length=3 , max_length=150 , description=  "Name of todo")
    todo_description:str = Field(... , description= "Describtion of todo" )
    todo_priority : Priority = Field(Priority.LOW , description= "Priority of Todo" )

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(... , description= "Unique identifier of the todo" )


class TodoUpdate(BaseModel):
    todo_name:Optional[str] = Field(None , min_length=3 , max_length=150 , description=  "Name of todo")
    todo_description: Optional[str] = Field(None , description= "Describtion of todo" )
    todo_priority : Optional[Priority] = Field(None , description= "Priority of Todo" )
    


all_todos = [
    Todo(todo_id =1 ,todo_name= "Sports" , todo_description = "Go to the gym" , todo_priority = Priority.MEDIUM ) , 
    Todo(todo_id =2 ,todo_name= "Read" , todo_description = "Read 10 pages" , todo_priority = Priority.HIGH ) ,     
    Todo(todo_id =3 ,todo_name= "Shop" , todo_description = "Go shoping" , todo_priority = Priority.LOW ) ,     
    Todo(todo_id =4 ,todo_name= "Study" , todo_description = "Study for exam" , todo_priority = Priority.HIGH ) , 
    Todo(todo_id =5 ,todo_name= "Meditate" , todo_description = "Meditate 20 min" , todo_priority = Priority.MEDIUM ) 
        ]

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id:int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
             return todo
    raise HTTPException(status_code=404,detail= "Todo not found" )   
      
@app.get("/todos" , response_model= List[Todo])
def get_todos(first_n:int =None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@app.post("/todos" , response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max([todoo.todo_id for todoo in all_todos])+1
    new_todo = Todo(todo_id = new_todo_id ,todo_name= todo.todo_name , todo_priority= todo.todo_priority , todo_description= todo.todo_description)
    all_todos.append(new_todo)
    return new_todo

@app.put("/todo/{todo_id}", response_model=Todo)
def update_todo(todo_id:int , updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            todo.todo_name = updated_todo.todo_name
            todo.todo_description = updated_todo.todo_description
            todo.todo_priority = updated_todo.todo_priority
            return todo
    raise HTTPException(status_code= 404 , detail = "Todo not found")

@app.delete("/todos")
def delete_todo(todo_id:int):
    for index , todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            delete_todo = all_todos.pop(index)
            return delete_todo
    raise HTTPException(status_code=404,detail= "Todo not found" )
    