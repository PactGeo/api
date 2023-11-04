from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class CommunityBase(BaseModel):
    name: str
    description: Optional[str] = None
    website: Optional[HttpUrl] = None

class CommunityCreate(CommunityBase):
    pass

class CommunityUpdate(CommunityBase):
    pass

class CommunityInDBBase(CommunityBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class Community(CommunityInDBBase):
    pass

# Schemas para relaciones (si es necesario)
class UserWithDebates(UserInDBBase):
    debates: List[Debate] = []

class CommunityWithMembers(CommunityInDBBase):
    members: List[User] = []