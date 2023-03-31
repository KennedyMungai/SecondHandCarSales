"""The schema file for the cars being sold"""
from typing import Optional
from pydantic import BaseModel, Field


class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}


class CarBase(MongoBaseModel):
    brand: str = Field(..., min_length=3)
    make: str = Field(..., min_length=3)
    year: int = Field(...)
    price: int = Field(...)
    km: int = Field(...)
    cm3: int = Field(...)


class CarUpdate(MongoBaseModel):
    price: Optional[int] = None