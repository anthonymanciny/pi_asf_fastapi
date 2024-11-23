from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base

# Tabela Instituicao
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


# Tabela EspacoInstituicao
class EspacoInstituicao(Base):
    __tablename__ = 'Espaco_Instituicao'

    ID_Espaco_Instituicao = Column(Integer, primary_key=True, autoincrement=True)
    ID_Instituicao = Column(Integer, ForeignKey('Instituicao_Social.ID_Instituicao', ondelete='CASCADE'))
    Nome_Espaco = Column(String(30), nullable=False)
    Capacidade = Column(Integer, nullable=False)
    Responsavel = Column(String(35), nullable=False)

    instituicao = relationship('Instituicao', back_populates='espacos')
    alocacoes = relationship('Alocacao', back_populates='espaco')


# Tabela Pessoa
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


# Tabela Alocacao
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


# Tabela Evento
class Evento(Base):
    __tablename__ = 'Eventos'

    ID_Evento = Column(Integer, primary_key=True, autoincrement=True)
    NomeEvento = Column(String(35), nullable=False)
    Responsavel_Evento = Column(String(35), nullable=False)
    Status = Column(Integer, nullable=False)

    alocacoes = relationship('Alocacao', back_populates='evento')
    participacoes = relationship('Participacao', back_populates='evento')


# Tabela Participacao
class Participacao(Base):
    __tablename__ = 'Participacao'

    ID_Participacao = Column(Integer, primary_key=True, autoincrement=True)
    ID_Evento = Column(Integer, ForeignKey('Eventos.ID_Evento', ondelete='CASCADE'))
    ID_Pessoa = Column(Integer, ForeignKey('Pessoas.ID_Pessoa', ondelete='CASCADE'))
    Tipo_Participacao = Column(String(1), nullable=False)

    evento = relationship('Evento', back_populates='participacoes')
    pessoa = relationship('Pessoa', back_populates='participacoes')

