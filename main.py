from fastapi import FastAPI
from routes import home, addres, pontos

app = FastAPI()
app.include_router(home.router)
app.include_router(addres.router)
app.include_router(pontos.router)