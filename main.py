from fastapi import FastAPI, Depends
from auth.security import verify_password

app = FastAPI(
    title="Meu primeiro fast API",
    version="1.0.0",
    description="Uma API simples para aprender FastAPI",
)

@app.get("/")
async def root(username: str = Depends(verify_password)):
    return {"message": f"Olá, {username}!"}
