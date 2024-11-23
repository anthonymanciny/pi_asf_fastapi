from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.Base import Base

class Instituicao(Base):
    __tablename__ = 'Instituicao_Social'

    ID_Instituicao = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(35), nullable=False)
    Email = Column(String(50), nullable=False)
    Endereco = Column(String(60), nullable=False)
    Telefone = Column(String(11), nullable=False)
    Observacao = Column(String(100), nullable=True)

    alocacoes = relationship('Alocacao', back_populates='instituicao')
    espacos = relationship('EspacoInstituicao', back_populates='instituicao')