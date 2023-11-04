from fastapi import APIRouter, Depends
from typing import List

from app.schemas import CommunityCreate, Community, CommunityUpdate  # Importa los esquemas de comunidad
from app.crud import get_communities, create_community, update_community, delete_community  # Importa las funciones CRUD

router = APIRouter()

@router.post("/communities/", response_model=Community)
async def create_new_community(community: CommunityCreate):
    # Lógica para crear una nueva comunidad
    return create_community(community)

@router.get("/communities/", response_model=List[Community])
async def read_communities(skip: int = 0, limit: int = 10):
    # Lógica para obtener una lista de comunidades
    return get_communities(skip=skip, limit=limit)

@router.put("/communities/{community_id}", response_model=Community)
async def update_existing_community(community_id: int, community: CommunityUpdate):
    # Lógica para actualizar una comunidad existente
    return update_community(community_id, community)

@router.delete("/communities/{community_id}", response_model=Community)
async def delete_existing_community(community_id: int):
    # Lógica para eliminar una comunidad
    return delete_community(community_id)
