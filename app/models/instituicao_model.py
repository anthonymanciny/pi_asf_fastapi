from sqlalchemy import Column, String, Integer, CHAR, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.Base import Base

#Tabela Instituicao
class Instituicao(Base):
    __tablename__ = 'Instituicao_Social'

    ID_Instituicao = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(35), nullable=False)
    Email = Column(String(50), nullable=False)
    Endereco = Column(String(60), nullable=False)
    Telefone = Column(CHAR(11), nullable=False)
    Observacao = Column(String(100), nullable=True)

    __table_args__ = (
        CheckConstraint('ID_Instituicao <= 9999999999', name='check_id_max_10_digits'),  
    )  #forma que achei para limitar caracteres numericos 

    alocacoes = relationship('Alocacao', back_populates='instituicao')
    espacos = relationship('EspacoInstituicao', back_populates='instituicao')
