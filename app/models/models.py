from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base


class Instituicao(Base):
    __tablename__ = 'instituicao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    email = Column('email', String, nullable=False)
    endereco = Column('endereco', String, nullable=False)
    telefone = Column('telefone', String, nullable=False)
    observacao = Column('observacao', String, nullable=True)  # Alterado para nullable=True

    # Relacionamento com alocacoes
    alocacoes = relationship('Alocacao', back_populates='instituicao')

    # Relacionamento com espaços
    espacos = relationship('EspacoInstituicao', back_populates='instituicao')


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    email = Column('email', String, nullable=True)
    telefone = Column('celular', String, nullable=True)
    cpf = Column('cpf', String, nullable=False)
    data_nascimento = Column('datanascimento', Date, nullable=True)
    genero = Column('genero', String, nullable=True)

    # Relacionamento com participações
    participacoes = relationship('Participacao', back_populates='pessoa')


class Evento(Base):
    __tablename__ = 'evento'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    datahora = Column('datahora', DateTime, nullable=False)
    responsavel_evento = Column('responsavel_evento', String, nullable=False)

    # Relacionamento com alocacoes
    alocacoes = relationship('Alocacao', back_populates='evento')

    # Relacionamento com participações
    participacoes = relationship('Participacao', back_populates='evento')


class Participacao(Base):
    __tablename__ = 'participacao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    # Chaves estrangeiras para as tabelas Evento e Pessoa
    id_evento = Column(Integer, ForeignKey('evento.id', ondelete='CASCADE'))
    id_pessoa = Column(Integer, ForeignKey('pessoa.id', ondelete='CASCADE'))

    # Relacionamentos com as tabelas Evento e Pessoa
    evento = relationship('Evento', back_populates='participacoes', foreign_keys=[id_evento])
    pessoa = relationship('Pessoa', back_populates='participacoes', foreign_keys=[id_pessoa])

    tipo = Column('tipo', String, nullable=False)


class EspacoInstituicao(Base):
    __tablename__ = 'espacoinstituicao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    # Chave estrangeira para Instituicao
    id_instituicao = Column(Integer, ForeignKey('instituicao.id', ondelete='CASCADE'))

    # Relacionamento com a tabela Instituicao
    instituicao = relationship("Instituicao", back_populates="espacos")

    nome = Column('nome', String, nullable=False)
    capacidade = Column('capacidade', Integer, nullable=False)  # Alterado para Integer
    responsavel = Column('responsavel', String, nullable=False)

    # Relacionamento com alocacoes
    alocacoes = relationship('Alocacao', back_populates='espaco')


class Alocacao(Base):
    __tablename__ = 'alocacao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    # Chaves estrangeiras para Evento, Instituicao e EspacoInstituicao
    id_evento = Column(Integer, ForeignKey('evento.id', ondelete='CASCADE'))
    id_instituicao = Column(Integer, ForeignKey('instituicao.id', ondelete='CASCADE'))
    id_espaco = Column(Integer, ForeignKey('espacoinstituicao.id', ondelete='CASCADE'))

    # Relacionamentos com as tabelas Evento, Instituicao e EspacoInstituicao
    evento = relationship('Evento', back_populates='alocacoes', foreign_keys=[id_evento])
    instituicao = relationship('Instituicao', back_populates='alocacoes', foreign_keys=[id_instituicao])
    espaco = relationship('EspacoInstituicao', back_populates='alocacoes', foreign_keys=[id_espaco])

    datahora = Column('datahora', DateTime, nullable=False)
    status = Column('status', String, nullable=False)
    responsavel_local = Column('responsavel_local', String, nullable=False)
