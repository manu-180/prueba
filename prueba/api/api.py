from fastapi import FastAPI, HTTPException, Depends, Response

app = FastAPI()

# Datos de usuarios (simulados para este ejemplo)
USERS = {
    "ivanna.risaro@hotmail.com": "123456789"
}

# Middleware para verificar la autenticación
def authenticate_user(email: str, password: str):
    if email in USERS and USERS[email] == password:
        return True
    return False

@app.post("/auth")
async def login_auth(email: str, password: str, response: Response):
    if authenticate_user(email, password):
        # Autenticación exitosa
        response.status_code = 200
        response.headers["Location"] = "/"  # Redirige a la página principal
        return {"message": "Autenticación exitosa"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")





async def hello(user:str) -> str:
    if user == "juli":
        return "hello juli"
    elif user == "cami":
        return "hello cami"
    elif user == "theo":
        return "hello theo"
    else:
        return "hello gentuza "
    
    
async def hello() -> str:
    return "Hello manu"

