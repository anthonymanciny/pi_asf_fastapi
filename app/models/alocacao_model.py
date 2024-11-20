from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.Base import Base

class Alocacao(Base):
    __tablename__ = 'alocacao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    id_evento = Column(Integer, ForeignKey('evento.id', ondelete='CASCADE'))
    id_instituicao = Column(Integer, ForeignKey('instituicao.id', ondelete='CASCADE'))
    id_espaco = Column(Integer, ForeignKey('espacoinstituicao.id', ondelete='CASCADE'))

    evento = relationship('evento', foreign_keys=[id_evento])
    instituicao = relationship('instituicao', foreign_keys=[id_instituicao])
    espaco = relationship('espacoInstituicao', foreign_keys=[id_espaco])

    datahora = Column('datahora', DateTime, nullable=False)
    status = Column('status', String, nullable=False)
    responsavel_local = Column('responsavel_local', String, nullable=False)