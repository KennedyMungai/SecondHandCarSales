"""The cars router"""
from fastapi import APIRouter


cars_router = APIRouter(prefix="/cars", tags=["Cars"])


@cars_router.get("/", response_description="List all the cats")
async def list_cars():
    return {"data": "All cars will go here"}
