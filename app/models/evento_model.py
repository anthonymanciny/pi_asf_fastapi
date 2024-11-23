from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.Base import Base

class Evento(Base):
    __tablename__ = 'Eventos'

    ID_Evento = Column(Integer, primary_key=True, autoincrement=True)
    NomeEvento = Column(String(35), nullable=False)
    Responsavel_Evento = Column(String(35), nullable=False)
    Status = Column(Integer, nullable=False)

    alocacoes = relationship('Alocacao', back_populates='evento')
    participacoes = relationship('Participacao', back_populates='evento')