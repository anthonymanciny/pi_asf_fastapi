from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base

class EspacoInstituicao(Base):
    __tablename__ = 'Espaco_Instituicao'

    ID_Espaco_Instituicao = Column(Integer, primary_key=True, autoincrement=True)
    ID_Instituicao = Column(Integer, ForeignKey('Instituicao_Social.ID_Instituicao', ondelete='CASCADE'))
    Nome_Espaco = Column(String(30), nullable=False)
    Capacidade = Column(Integer, nullable=False)
    Responsavel = Column(String(35), nullable=False)

    instituicao = relationship('Instituicao', back_populates='espacos')
    alocacoes = relationship('Alocacao', back_populates='espaco')