from sqlalchemy import Column, String, Integer, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.Base import Base

#Tabela Evento
class Evento(Base):
    __tablename__ = 'Eventos'

    ID_Evento = Column(Integer, primary_key=True, autoincrement=True)
    NomeEvento = Column(String(35), nullable=False)
    Responsavel_Evento = Column(String(35), nullable=False)
    Status = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('ID_Evento <= 9999999999', name='check_IDEvento_max_10_digits'),
        CheckConstraint('Status IN (1, 2, 3, 4)', name='check_status_valid_values')

    )

    alocacoes = relationship('Alocacao', back_populates='evento')
    participacoes = relationship('Participacao', back_populates='evento')
