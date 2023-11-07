from typing import Generator
from app.database import SessionLocal

# Dependencia para inyectar una sesión de base de datos en las rutas
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
