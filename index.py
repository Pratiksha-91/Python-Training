from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from datetime import datetime
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr


app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client["Demo"]
usercollection = db["users"]


#create one  class with variables with their types and validations
class CreateUserRequest(BaseModel):
    name: str
    password: str
    email: EmailStr

#Creating account for new candiate
@app.post("/sign-up/")
async def create_user(user_data: CreateUserRequest):
    
    if usercollection.find_one({"mail": user_data.email}):
        return {"message": "User already exists!"}
    else:
        
        user_document = {
            "name": user_data.name,
            "password": user_data.password,
            "mail": user_data.email,
            "user_type": "Candidate",
            "created_at": datetime.today().strftime("%Y-%m-%d")
        }
        result = usercollection.insert_one(user_document)
        if not result.acknowledged:
            raise HTTPException(status_code=500, detail="Failed to insert user into database")

        return {"message": "User created successfully"}
    


#Login if allready have a account
@app.get("/login/")
async def user_login(mail: str, password: str):
    user = usercollection.find_one({"mail": mail, "password": password})
    if user:
          
          user_type = user.get("user_type")
          print(user_type)

          if user_type == "Admin":
               #AdminDash()
              return JSONResponse(content={"redirect_url": "/admindash.py"})
          elif user_type == "Candidate":
               return JSONResponse(content={"redirect_url": "/candidatedash.py"})
          else:
               return "Invalid Login"
               
               
    else:
          return {"not found"}



