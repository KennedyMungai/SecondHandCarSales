"""The schema file for the cars being sold"""
from pydantic import BaseModel, Field


class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}