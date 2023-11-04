from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database import Base

class Debate(Base):
    __tablename__ = "debates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    community_id = Column(Integer, ForeignKey('communities.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    # Agrega otros campos que necesites
