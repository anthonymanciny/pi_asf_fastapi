from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, CHAR, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.Base import Base

# Tabela Instituicao
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


# Tabela EspacoInstituicao
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


# Tabela Pessoa
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

    __table_args__ = (
        CheckConstraint('ID_Alocacao <= 9999999999', name='check_IDAlocacao_max_10_digits'),
        CheckConstraint('Status IN (1, 2, 3)', name='check_status_aloc_valid_values'),  #Restrição para valores 1, 2 ou 3

    )

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

    __table_args__ = (
        CheckConstraint('ID_Evento <= 9999999999', name='check_IDEvento_max_10_digits'),
        CheckConstraint('Status IN (1, 2, 3, 4)', name='check_status_valid_values')

    )

    alocacoes = relationship('Alocacao', back_populates='evento')
    participacoes = relationship('Participacao', back_populates='evento')


# Tabela Participacao
class Participacao(Base):
    __tablename__ = 'Participacao'

    ID_Participacao = Column(Integer, primary_key=True, autoincrement=True)
    ID_Evento = Column(Integer, ForeignKey('Eventos.ID_Evento', ondelete='CASCADE'))
    ID_Pessoa = Column(Integer, ForeignKey('Pessoas.ID_Pessoa', ondelete='CASCADE'))
    tipo_participacao = Column(CHAR(1), nullable=False)

    __table_args__ = (
        CheckConstraint('ID_Participacao <= 9999999999', name='check_IDParticipacao_max_10_digits'),
        CheckConstraint('tipo_participacao IN (1, 2)', name='check_participacao_valid_values')

    )

    evento = relationship('Evento', back_populates='participacoes')
    pessoa = relationship('Pessoa', back_populates='participacoes')

