from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base


class Pessoa(Base):
    __tablename__ = 'Pessoas'

    ID_Pessoa = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(35), nullable=False)
    Senha = Column(String(35), nullable=False)
    Email = Column(String(50), unique=True, nullable=True)
    Celular = Column(String(11), nullable=True)
    Telefone = Column(String(11), nullable=True)
    CPF = Column(String(11), unique=True, nullable=False)
    DataNasc = Column(Date, nullable=True)
    Genero = Column(String(1), nullable=True)

    participacoes = relationship('Participacao', back_populates='pessoa')