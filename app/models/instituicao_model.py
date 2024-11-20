from sqlalchemy import Column, String, Integer
from app.db.Base import Base

class Instituicao(Base):
    __tablename__ = 'instituicao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    email = Column('email', String, nullable=False)
    endereco = Column('endereco', String, nullable=False)
    telefone = Column('telefone', String, nullable=False)
    observacao = Column('observacao', String, nullable=True)  # Alterado para nullable=True
