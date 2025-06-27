from fastapi import FastAPI

api = FastAPI()

data = [
    {"todo_id":1 , "todo_name":"sport" , "todo_describtion":"go to gym"   }
    {"todo_id":2 , "todo_name":"read" , "todo_describtion":"read 10 pages"   }
    {"todo_id":1 , "todo_name":"shop" , "todo_describtion":"go shoping"   }
    {"todo_id":1 , "todo_name":"study" , "todo_describtion":"study for exam"   }
    {"todo_id":1 , "todo_name":"meditate" , "todo_describtion":"meditate 20 min"   }
        ]
#GET, POST,PUT,DELETE
@api.get('/')
def index():
    return {"message":"Hello World"}