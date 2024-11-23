from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.Base import Base

class Alocacao(Base):
    __tablename__ = 'Alocacao'

    ID_Alocacao = Column(Integer, primary_key=True, autoincrement=True)
    ID_Evento = Column(Integer, ForeignKey('Eventos.ID_Evento', ondelete='CASCADE'))
    ID_Instituicao = Column(Integer, ForeignKey('Instituicao_Social.ID_Instituicao', ondelete='CASCADE'))
    ID_Espaco_Instituicao = Column(Integer, ForeignKey('Espaco_Instituicao.ID_Espaco_Instituicao', ondelete='CASCADE'))
    DataHora = Column(DateTime, nullable=False)
    Status = Column(Integer, nullable=False)
    Responsavel_Local = Column(String(35), nullable=False)

    evento = relationship('Evento', back_populates='alocacoes')
    instituicao = relationship('Instituicao', back_populates='alocacoes')
    espaco = relationship('EspacoInstituicao', back_populates='alocacoes')