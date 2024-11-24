from sqlalchemy import Column, String, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.Base import Base

#Tabela EspacoInstituicao
class EspacoInstituicao(Base):
    __tablename__ = 'Espaco_Instituicao'

    ID_instituicao = Column(Integer, ForeignKey('Instituicao_Social.ID_Instituicao', ondelete='CASCADE'))
    ID_espaco_instituicao = Column(Integer, primary_key=True, autoincrement=True)
    Nome_espaco = Column(String(30), nullable=False)
    Capacidade = Column(Integer, nullable=False)
    Responsavel = Column(String(35), nullable=False)

    __table_args__ = (
        CheckConstraint('ID_espaco_instituicao <= 9999999999', name='check_IDEspaco_max_10_digits'), 
        CheckConstraint('Capacidade <= 99999', name='check_IDCapacidade_max_5_digits'), 

    )


    instituicao = relationship('Instituicao', back_populates='espacos')
    alocacoes = relationship('Alocacao', back_populates='espaco')
