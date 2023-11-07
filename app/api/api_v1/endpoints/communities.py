from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.post("/communities/", response_model=schemas.Community)
def create_community(community: schemas.CommunityCreate, db: Session = Depends(deps.get_db)):
    return crud.create_community(db=db, community=community)

@router.get("/communities/{community_id}", response_model=schemas.Community)
def read_community(community_id: int, db: Session = Depends(deps.get_db)):
    db_community = crud.get_community(db, community_id=community_id)
    if db_community is None:
        raise HTTPException(status_code=404, detail="Community not found")
    return db_community