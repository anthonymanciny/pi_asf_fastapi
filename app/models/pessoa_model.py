from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False,)
    email = Column('email', String, nullable=True)
    telefone = Column('celular', String, nullable=True)
    cpf = Column('cpf', String, nullable=False)
    data_nascimento = Column('datanascimento', Date, nullable=True)
    genero = Column('genero', String, nullable=True)
