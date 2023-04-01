"""The cars router"""
from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from schemas.cars_schema import CarBase

cars_router = APIRouter(prefix="/cars", tags=["Cars"])


@cars_router.get("/", response_description="List all the cats")
async def list_cars():
    """The root endpoint for the cars endpoint

    Returns:
        dict: A dictionary to show the data to be returned
    """
    return {"data": "All cars will go here"}


@cars_router.post("/", response_description="Add a new car")
async def create_car(_request: Request, _car: CarBase = Body(...)):
    _car = jsonable_encoder(_car)
    _new_car = await _request.app.mongodb["cars1"].insert_one(_car)
    _created_car = await _request.app.mongodb["cars1"].find_one({"_id": _new_car.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=_created_car)
