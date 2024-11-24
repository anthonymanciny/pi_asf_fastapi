from sqlalchemy import Column, String, Integer, Date, CHAR, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.Base import Base


#Tabela Pessoa
class Pessoa(Base):
    __tablename__ = 'Pessoas'

    ID_Pessoa = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(35), nullable=False)
    Senha = Column(String(60), nullable=False) #Pra colocar tipo password eu vi que so usando salt e hash (sugestion)
    Email = Column(String(50), unique=True, nullable=False)
    Celular = Column(CHAR(11), unique=True, nullable=False) #adicionei unique aqui
    Telefone = Column(CHAR(11), unique=True, nullable=True) #e aqui
    CPF = Column(CHAR(11), unique=True, nullable=False)
    DataNasc = Column(Date, nullable=False)
    Genero = Column(CHAR(1), nullable=True)

    __table_args__ = (
        CheckConstraint('ID_Pessoa <= 9999999999', name='check_IDPessoa_max_10_digits'),
        CheckConstraint('Genero IN ("1", "2")', name='check_genero_valid_values'),  # Restrição para valores M ou F (Sugestao mudar pra M ou F)

    )

    participacoes = relationship('Participacao', back_populates='pessoa')
