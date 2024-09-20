from functools import wraps

from core.db_manager import SessionLocal
from core.deps import SessionDep


def transactional():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            db: SessionDep = kwargs.get('db')
            if db is None:
                db = SessionLocal()
                kwargs['db'] = db
                print("Creating DB", db)
            try:
                result = func(*args, **kwargs)
                print("Committing DB", db)
                db.commit()
                return result
            except:
                print("Rolling back DB", db)
                db.rollback()

        return wrapper

    return decorator
