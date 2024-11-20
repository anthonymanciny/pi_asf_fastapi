# from typing import Annotated
# from fastapi import Depends
# from sqlalchemy.orm import Session

# def db_session():
#     try:
#         session = Session()
#         yield session
#     finally:
#         session.close()





# SessionDep = Annotated[Session, Depends(db_session)]



# depends.py

from sqlalchemy.orm import Session
from .connection import SessionLocal

# Função que retorna uma sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
