from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    profile_image = Column(String)
    # Agrega otros campos que necesites
