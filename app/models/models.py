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

    alocacoes = relationship('Alocacao', back_populates='instituicao')


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    email = Column('email', String, nullable=True)
    telefone = Column('celular', String, nullable=True)
    cpf = Column('cpf', String, nullable=False)
    data_nascimento = Column('datanascimento', Date, nullable=True)
    genero = Column('genero', String, nullable=True)


class Evento(Base):
    __tablename__ = 'evento'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    datahora = Column('datahora', DateTime, nullable=False)
    responsavel_evento = Column('responsavel_evento', String, nullable=False)

    alocacoes = relationship('Alocacao', back_populates='evento')


class Participacao(Base):
    __tablename__ = 'participacao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    id_evento = Column(Integer, ForeignKey('evento.id', ondelete='CASCADE'))
    id_pessoa = Column(Integer, ForeignKey('pessoa.id', ondelete='CASCADE'))

    evento = relationship('Evento', foreign_keys=[id_evento])
    pessoa = relationship('Pessoa', foreign_keys=[id_pessoa])

    tipo = Column('tipo', String, nullable=False)


class EspacoInstituicao(Base):
    __tablename__ = 'espacoinstituicao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    id_instituicao = Column(Integer, ForeignKey('instituicao.id', ondelete='CASCADE'))
    instituicao = relationship('Instituicao', foreign_keys=[id_instituicao])

    nome = Column('nome', String, nullable=False)
    capacidade = Column('capacidade', Integer, nullable=False)  # Alterado para Integer
    responsavel = Column('responsavel', String, nullable=False)

    alocacoes = relationship('Alocacao', back_populates='espaco')


class Alocacao(Base):
    __tablename__ = 'alocacao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    id_evento = Column(Integer, ForeignKey('evento.id', ondelete='CASCADE'))
    id_instituicao = Column(Integer, ForeignKey('instituicao.id', ondelete='CASCADE'))
    id_espaco = Column(Integer, ForeignKey('espacoinstituicao.id', ondelete='CASCADE'))

    evento = relationship('Evento', back_populates='alocacoes', foreign_keys=[id_evento])
    instituicao = relationship('Instituicao', back_populates='alocacoes', foreign_keys=[id_instituicao])
    espaco = relationship('EspacoInstituicao', back_populates='alocacoes', foreign_keys=[id_espaco])

    datahora = Column('datahora', DateTime, nullable=False)
    status = Column('status', String, nullable=False)
    responsavel_local = Column('responsavel_local', String, nullable=False)
