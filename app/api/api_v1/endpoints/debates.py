from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.post("/debates/", response_model=schemas.Debate)
def create_debate(debate: schemas.DebateCreate, db: Session = Depends(deps.get_db)):
    return crud.create_debate(db=db, debate=debate)

@router.get("/debates/{debate_id}", response_model=schemas.Debate)
def read_debate(debate_id: int, db: Session = Depends(deps.get_db)):
    db_debate = crud.get_debate(db, debate_id=debate_id)
    if db_debate is None:
        raise HTTPException(status_code=404, detail="Debate not found")
    return db_debate