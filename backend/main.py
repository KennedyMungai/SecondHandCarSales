"""The main app for the backend of the webapp"""
import os

import uvicorn
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routers.cars import cars_router

load_dotenv(find_dotenv())

DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    """The connection function"""
    app.mongodb_client = AsyncIOMotorClient(DB_URL)


@app.on_event("shutdown")
async def shutdown_db_client():
    """The database connection method
    """
    app.mongodb_client.close()


@app.get("/")
async def root() -> dict:
    """The disconnection function

    Returns:
        dict: _description_
    """
    return {'Message': 'This API works'}


@app.include_router(cars_router)
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )
