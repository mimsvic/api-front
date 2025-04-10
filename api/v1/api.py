from fastapi import APIRouter
from api.v1.endpoints import office_characters  

api_router = APIRouter()
api_router.include_router(office_characters.router, prefix="/office-character", tags=["Characters"])
