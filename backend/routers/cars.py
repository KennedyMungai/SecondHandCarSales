"""The cars router"""
from fastapi import APIRouter


cars_router = APIRouter(prefix="/cars", tags=["Cars"])
