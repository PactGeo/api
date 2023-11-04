from sqlalchemy import Column, Integer, String
from app.database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    code = Column(String, unique=True, index=True)  # ISO country codes, e.g., 'US' for the United States
    # Agrega aquí más campos si es necesario
