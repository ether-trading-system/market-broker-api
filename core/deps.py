from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from core.db_manager import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        print("Closing DB", db)
        db.close()


SessionDep = Annotated[Session, Depends(get_db)]
