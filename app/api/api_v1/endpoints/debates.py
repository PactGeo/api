from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Debate)
def create_debate(debate: schemas.DebateCreate, db: Session = Depends(deps.get_db)):
    return crud.create_debate(db=db, debate=debate)

@router.get("/{debate_id}", response_model=schemas.Debate)
def read_debate(debate_id: int, db: Session = Depends(deps.get_db)):
    db_debate = crud.get_debate(db, debate_id=debate_id)
    if db_debate is None:
        raise HTTPException(status_code=404, detail="Debate not found")
    return db_debate

@router.put("/debates/{debate_id}", response_model=schemas.Debate)
def update_debate(
    *,
    db: Session = Depends(deps.get_db),
    debate_id: int,
    debate_in: schemas.DebateUpdate
):
    db_debate = crud.get_debate(db, debate_id=debate_id)
    if not db_debate:
        raise HTTPException(status_code=404, detail="Debate not found")
    debate = crud.update_debate(db=db, debate_id=debate_id, debate=debate_in)
    return debate

@router.delete("/debates/{debate_id}", response_model=schemas.Debate)
def delete_debate(
    *,
    db: Session = Depends(deps.get_db),
    debate_id: int
):
    db_debate = crud.get_debate(db, debate_id=debate_id)
    if not db_debate:
        raise HTTPException(status_code=404, detail="Debate not found")
    crud.delete_debate(db=db, debate_id=debate_id)
    return db_debate
