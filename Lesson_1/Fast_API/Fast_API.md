You find the resources for this lesson [here](https://www.youtube.com/watch?v=rvFsGRvj9jo)

# What is an API?
IT is a set of rules that allows different software applications to communicate with each other.

# What do we mean by framework? 
A framework is a pre-written collection of code, tools, and best practices that helps developers build software more efficiently and consistently.

# What is fast API?
So fast api is a framework that allows us to build such apis easily. The key feature of fast API is that it is build for high performance by using asynchronius servers, which means it can handle multiple connections at once. 

# What is REST API?
A REST API (Representational State Transfer Application Programming Interface) is a way for software applications to communicate over the web using standard HTTP methods (like GET, POST, PUT, DELETE). It's one of the most common ways to build web services. 

# REST full api? 
A RESTful API refers to an API that adheres to the principles and constraints of REST (Representational State Transfer). Essentially, it's an implementation of a web service that follows REST principles to provide a stateless, client-server interaction using standard HTTP methods.

# Fast API is a REST full api
Fast API is a REST full api meaning that it support standard HTML methods like get, post , put and delete.

# Function decorators: 
A function decorator in Python is a design pattern that allows you to modify or enhance the behavior of a function without changing its code. Decorators are often used for things like logging, access control, memoization (caching), timing, and more.

**Example**

```python 
def my_decorator(my_func):
    def wrapper(): 
        print("Something is happening before the function call!")
        my_func()
        print("Something is happening after the function call!")
    return wrapper

@my_decorator
def print_hello():
   print("hello") 

if __name__ == "__main__":
    print_hello()

```
The wrapper is a nested function inside a decorator. It's the function that replaces the original function when you apply a decorator.

Here’s what’s happening conceptually:

```py
def decorator(original_function):
    def wrapper():
        # Do something before
        original_function()
        # Do something after
    return wrapper
```

# Implementation of Fast API
First of all you need to install fast api. You do this py typing: 
`pip install fastapi` or if you use jupyter notebook or google colab you can use `!pip install fastapi`. 



Then we need to import it. 
```python
from fastapi import FastAPI
```
We need to instansiate it with some name: 
```
app = FastAPI()
```

Then we need to use decorator for Implementing the HTTP methods. 

## GET method
```py
@app.get("/") #"/" is root end point, when you open the localehost:1234 it will go to this end point
def say_hello_world()
    return {"message":"Hello World!"}

# You can also use different endpoint
@app.get("/todos")
def get_todos():
    return data  #assuming the data is a list of dictionaries.
``` 
This function can accept parameters too, in two ways: 
1. **Path parameter**: It is a part of the path and must be inside curly brakades.
for example:

```py
#You can pass the parameter by directely passing it to the path like localhost:1234/todos/2
@app.get("/todos/{first_n}")
def get_todos(first_n = None):
    if first_n:
        return data[:int(first_n)] # You have to get the int of the first_n because the object that is recieves in the function is not int.
    else:
        return data
``` 

2. **Query Parameters** Query parameters is like a query you write a question mark followed by parameters name and pass the value. 

For example: 

```py
# You write it like a query localhost:1234/todos?first_n=2
@app.get('/todos')
def get_todos(first_n = None):
    if first_n:
        return data[:first_n]
    else:
        return data
``` 
The code above will give you exception because you need  the first_n is treated as string not int and string we cannot use for sclicing the list. We need to type cast it by defining the type in the function declaration e.g `def get_todos(first_n:int = None):` and if the input is not a string it will give an exception.




If you want to write it asynchroniously use async in the begining and the await and the rest of the code. 

Example : 
```py

@app.get('/todos')
async def get_todos(first_n = None):
    await 
    if first_n:
        return data[:int(first_n)]
    else:
        return data
``` 

## POST method




# How to run the code
Put your code in a python file and call it whatever you like, in our case we call it main.py.
There is two way to run the code: 
## Method 1

In terminal write: 
```cmd
uviron main:app
```
so `uviron your_python_codes_name:your_fast_api_instance_name`. 
You call also specify port by adding `--port`

**Example:**
```cmd
uviron main:app --port 1234
```


## Method 2
In newer fastapi package we can use the following: 

```cmd
fastapi dev main.py --port 1234
```
