from fastapi import FastAPI

app = FastAPI()

all_todos = [
    {"todo_id":1 , "todo_name":"sport" , "todo_describtion":"go to gym"   },
    {"todo_id":2 , "todo_name":"read" , "todo_describtion":"read 10 pages"   },
    {"todo_id":3 , "todo_name":"shop" , "todo_describtion":"go shoping"   },
    {"todo_id":4 , "todo_name":"study" , "todo_describtion":"study for exam"   },
    {"todo_id":5 , "todo_name":"meditate" , "todo_describtion":"meditate 20 min"   }
        ]
#GET, POST,PUT,DELETE
@app.get('/')
def index():
    return {"message":"Hello World"}

#localhost:9999/2
@app.get('/todos/{todo_id}')
def get_todo(todo_id):
    for todo in all_todos:
        if todo["todo_id"]== int(todo_id):
            return {"result" : todo }
        
@app.get('/todos')
def get_todos(first_n = None):
    if first_n:

        return all_todos[:int(first_n)] 
    else:
        return all_todos

@app.post("/todos")
def create_todo(n_todo:dict): #assuming the provided data is {"todo_name": . , "todo_describtion": "..."}
    new_todo_id = max([todo["todo_id"] for todo in all_todos])+1
    new_todo = {
        "todo_id" : new_todo_id,
        "todo_name" : n_todo["todo_name"],
        "todo_describtion" : n_todo["todo_describtion"]
    }
    
    all_todos.append(new_todo)
    return new_todo
if __name__ == "__main__":
    print(all_todos[:2])