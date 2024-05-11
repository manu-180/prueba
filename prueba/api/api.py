async def hello(user:str) -> str:
    if user == "juli":
        return "hello juli"
    elif user == "cami":
        return "hello cami"
    elif user == "theo":
        return "hello theo"
    else:
        return "hello gente "
    
    
async def hello() -> str:
    return "Hello manu"