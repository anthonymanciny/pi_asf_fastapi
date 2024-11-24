from sqlalchemy import Column, Integer, ForeignKey, CHAR, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.Base import Base

#Tabela Participacao
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

