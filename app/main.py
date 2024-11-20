from fastapi import FastAPI
from app.routes.aapp_router import api_router

app = FastAPI()


@app.get('/')
def root():
    return "ok"

app.include_router(api_router)


# main.py

# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from app.db.depends import get_db
# from app.models.models import Pessoa  # Supondo que você tenha uma tabela 'Pessoa' definida em um arquivo models.py

# app = FastAPI()

# @app.get("/pessoas/")
# def list_pessoas(db: Session = Depends(get_db)):
#     return db.query(Pessoa).all()