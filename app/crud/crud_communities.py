from sqlalchemy.orm import Session
from app import models, schemas

def get_community(db: Session, community_id: int):
    return db.query(models.Community).filter(models.Community.id == community_id).first()

def get_communities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Community).offset(skip).limit(limit).all()

def create_community(db: Session, community: schemas.CommunityCreate):
    db_community = models.Community(**community.dict())
    db.add(db_community)
    db.commit()
    db.refresh(db_community)
    return db_community

def update_community(db: Session, community_id: int, community: schemas.CommunityUpdate):
    db_community = get_community(db, community_id)
    if db_community:
        update_data = community.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_community, key, value)
        db.commit()
        db.refresh(db_community)
    return db_community

def delete_community(db: Session, community_id: int):
    db_community = get_community(db, community_id)
    if db_community:
        db.delete(db_community)
        db.commit()
    return db_community
