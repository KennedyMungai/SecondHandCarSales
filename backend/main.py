"""The main app for the backend of the webapp"""
from fastapi import FastAPI
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)

@app.get("/")
async def root() -> dict:
    return {'Message': 'This API works'}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )