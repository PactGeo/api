from typing import Optional
from pydantic import BaseModel

class DebateBase(BaseModel):
    title: str
    description: Optional[str] = None

class DebateCreate(DebateBase):
    pass

class DebateUpdate(DebateBase):
    pass

class DebateInDBBase(DebateBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class Debate(DebateInDBBase):
    pass