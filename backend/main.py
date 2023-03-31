"""The main app for the backend of the webapp"""
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {'Message': 'This API works'}