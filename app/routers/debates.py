from fastapi import APIRouter, Depends
from typing import List

from app.schemas import DebateCreate, Debate, DebateUpdate  # Importa los esquemas de debate
from app.crud import get_debates, create_debate, update_debate, delete_debate  # Importa las funciones CRUD

router = APIRouter()

@router.post("/debates/", response_model=Debate)
async def create_new_debate(debate: DebateCreate):
    # Lógica para crear un nuevo debate
    return create_debate(debate)

@router.get("/debates/", response_model=List[Debate])
async def read_debates(skip: int = 0, limit: int = 10):
    # Lógica para obtener una lista de debates
    return get_debates(skip=skip, limit=limit)

@router.put("/debates/{debate_id}", response_model=Debate)
async def update_existing_debate(debate_id: int, debate: DebateUpdate):
    # Lógica para actualizar un debate existente
    return update_debate(debate_id, debate)

@router.delete("/debates/{debate_id}", response_model=Debate)
async def delete_existing_debate(debate_id: int):
    # Lógica para eliminar un debate
    return delete_debate(debate_id)
