from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base

class EspacoInstituicao(Base):
    __tablename__ = 'espacoinstituicao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    id_instituicao = Column(Integer, ForeignKey('instituicao.id', ondelete='CASCADE'))
    instituicao = relationship('Instituicao', foreign_keys=[id_instituicao])

    nome = Column('nome', String, nullable=False)
    capacidade = Column('capacidade', Integer, nullable=False)  # Alterado para Integer
    responsavel = Column('responsavel', String, nullable=False)