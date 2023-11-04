from app.models.user import Base as UserBase
from app.models.community import Base as CommunityBase
from app.models.debate import Base as DebateBase
from app.database import engine

def create_tables():
    UserBase.metadata.create_all(bind=engine)
    CommunityBase.metadata.create_all(bind=engine)
    DebateBase.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
