from sqlalchemy.orm import Session
from app import models, schemas

def get_debate(db: Session, debate_id: int):
    return db.query(models.Debate).filter(models.Debate.id == debate_id).first()

def get_debates(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Debate).offset(skip).limit(limit).all()

def create_debate(db: Session, debate: schemas.DebateCreate):
    db_debate = models.Debate(**debate.dict())
    db.add(db_debate)
    db.commit()
    db.refresh(db_debate)
    return db_debate

def update_debate(db: Session, debate_id: int, debate: schemas.DebateUpdate):
    db_debate = get_debate(db, debate_id)
    if db_debate:
        update_data = debate.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_debate, key, value)
        db.commit()
        db.refresh(db_debate)
    return db_debate

def delete_debate(db: Session, debate_id: int):
    db_debate = get_debate(db, debate_id)
    if db_debate:
        db.delete(db_debate)
        db.commit()
    return db_debate
