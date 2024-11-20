from sqlalchemy import Column, String, Integer, DateTime
from app.db.Base import Base

class Evento(Base):
    __tablename__ = 'evento'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    datahora = Column('datahora', DateTime, nullable=False)
    responsavel_evento = Column('responsavel_evento', String, nullable=False)
