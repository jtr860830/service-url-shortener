from fastapi import FastAPI

# from app import config

app: FastAPI = FastAPI()


@app.on_event("startup")
async def initialize():
    pass


@app.on_event("shutdown")
async def cleanup():
    pass


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}
