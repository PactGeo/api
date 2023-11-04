from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app import dependencies  # Importa las dependencias necesarias, como get_current_user
from app.schemas import UserCreate, User, UserUpdate  # Importa los esquemas de usuario
from app.crud import get_users, create_user, update_user, delete_user  # Importa las funciones CRUD

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_new_user(user: UserCreate):
    # Lógica para crear un nuevo usuario
    return create_user(user)

@router.get("/users/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 10):
    # Lógica para obtener una lista de usuarios
    return get_users(skip=skip, limit=limit)

@router.put("/users/{user_id}", response_model=User)
async def update_existing_user(user_id: int, user: UserUpdate):
    # Lógica para actualizar un usuario existente
    return update_user(user_id, user)

@router.delete("/users/{user_id}", response_model=User)
async def delete_existing_user(user_id: int):
    # Lógica para eliminar un usuario
    return delete_user(user_id)
