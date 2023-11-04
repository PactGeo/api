from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Community(Base):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(Integer)
    parent_id = Column(Integer, ForeignKey('communities.id'))
    
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship("Country")
    # Agrega otros campos que necesites
