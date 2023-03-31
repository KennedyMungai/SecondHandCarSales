"""The main app for the backend of the webapp"""
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)

@app.get("/")
async def root() -> dict:
    return {'Message': 'This API works'}