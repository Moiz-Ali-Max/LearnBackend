
#FastAPI:
"""
FastAPI is a python framwork that helps you build APIs quickly and easily.
It’s used in the backend to receive data from the frontend.
Like websites or apps), process it, and send back a response.
"""
#Standard way to create a fastapi app:
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
#@app.get("/") / -> It is also called as root path or home path
# def func1():
#     try:
#         return {
#             "status" : "success",
#             "data" : {
#                 "id" : 1,
#                 "name" : "moiz",
#                 "age" : 22,
#                 "email" : "moiz@gmail.com"
#             }
#         }
#     except Exception as e:
#         return {
#             "message" : str(e),
#             "status" : 500,
#             "data" : None  
#         }

###########################################################################################################

#How e receive data from frontend:
#1. Path Paramter:
"""
When you send data directly inside the URL path.
It uses when we want to get or delete a specific item (like user, product, etc.)
"""

# from fastapi import FastAPI


# app = FastAPI()
# @app.get("/user/{id}/{name}/{age}/{email}")
# def func1(id: int, name, age, email):
#     try:
#         return {
#             "status" : "success",
#             "data" : {
#                 "id" : id,
#                 "name" : name,
#                 "age" : age,
#                 "email" : email
#             }
#         }
#     except Exception as e:
#         return {
#             "message" : str(e),
#             "status" : 500,
#             "data" : None  
#         }

##########################################################################################################

#2. Query Parameter:
"""
When you send data after the ? in URL. Like key-value pairs.
Uses: For searching, filtering, or optional info.
"""
# from fastapi import FastAPI


# app = FastAPI()

# @app.get("/user")
# def func1(query, name, city, address):
#     try:
#         return {
#             "status" : "success",
#             "data" : {
#                 "q" : query,
#                 "name" : name,
#                 "city" : city,
#                 "address" : address
#             }
#         }
#     except Exception as e:
#         return {
#             "message" : str(e),
#             "status" : 500,
#             "data" : None  
#         }
        
########################################################################################################      
#3. Body Parameter:
"""
When you send data inside the body of the request — usually in JSON format.
It is secure and allows sending complex data.
It is used for creating or updating data.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id : Optional [int] = None
    name: str
    age : int
    email : str
    address : str
    college : str
    country : str


@app.get("/user/{id}")
def func1(id, user : User, query : Optional[str] = None):
    try:
        return {
            "status" : "success",
            "data" : {
                "id" : id,
                "query" : query,
                "user" : user
            }
        }
    except Exception as e:
        return {
            "message" : str(e),
            "status" : 500,
            "data" : None  
        }




