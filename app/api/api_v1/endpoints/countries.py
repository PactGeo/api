from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    countries = crud.get_countries(db, skip=skip, limit=limit)
    return countries

@router.post("/", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(deps.get_db)):
    db_country = crud.create_country(db, country=country)
    return db_country

@router.get("/{country_id}", response_model=schemas.Country)
def read_country(country_id: int, db: Session = Depends(deps.get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country
