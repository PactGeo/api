from sqlalchemy.orm import Session
from app.models.country import Country
from app.schemas.country import CountryCreate

def get_country(db: Session, country_id: int):
    return db.query(Country).filter(Country.id == country_id).first()

def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: CountryCreate):
    db_country = Country(name=country.name, code=country.code)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country
