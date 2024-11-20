from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.Base import Base

class Participacao(Base):
    __tablename__ = 'participacao'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)

    id_evento = Column(Integer, ForeignKey('evento.id', ondelete='CASCADE'))
    id_pessoa = Column(Integer, ForeignKey('pessoa.id', ondelete='CASCADE'))

    evento = relationship('evento', foreign_keys=[id_evento])
    pessoa = relationship('pessoa', foreign_keys=[id_pessoa])

    tipo = Column('tipo', String, nullable=False)