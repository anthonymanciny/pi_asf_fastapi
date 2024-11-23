from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base

class Participacao(Base):
    __tablename__ = 'Participacao'

    ID_Participacao = Column(Integer, primary_key=True, autoincrement=True)
    ID_Evento = Column(Integer, ForeignKey('Eventos.ID_Evento', ondelete='CASCADE'))
    ID_Pessoa = Column(Integer, ForeignKey('Pessoas.ID_Pessoa', ondelete='CASCADE'))
    Tipo_Participacao = Column(String(1), nullable=False)

    evento = relationship('Evento', back_populates='participacoes')
    pessoa = relationship('Pessoa', back_populates='participacoes')
