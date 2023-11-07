from fastapi import APIRouter

from app.api.api_v1.endpoints import communities, debates, users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(communities.router, prefix="/communities", tags=["communities"])
api_router.include_router(debates.router, prefix="/debates", tags=["debates"])
