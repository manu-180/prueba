from fastapi import FastAPI, HTTPException, status 
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Datos de usuarios (simulados para este ejemplo)
USERS = {
    "ivanna.risaro@hotmail.com": "123456789"
}

class Login(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    user: str
    permissions: List[str]
    message: str

@app.post("/login", response_model=LoginResponse)
def authenticate():
    raise HTTPException(status_code=status.HTTP_200_OK)
    




async def hello(user:str) -> str:
    if user == "juli":
        return "hello juli"
    elif user == "cami":
        return "hello cami"
    elif user == "theo":
        return "hello theo"
    else:
        return "hello gente "
    
    
async def hello_manu() -> str:
    return "Hello manu"

