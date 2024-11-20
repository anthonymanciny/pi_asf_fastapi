from pydantic import BaseModel
from typing import Optional


class ParticipacaoBase(BaseModel):
    id_evento: int
    id_pessoa: int
    tipo: str


class ParticipacaoCreate(ParticipacaoBase):
    pass


class ParticipacaoUpdate(BaseModel):
    id_evento: Optional[int]
    id_pessoa: Optional[int]
    tipo: Optional[str]


class ParticipacaoResponse(ParticipacaoBase):
    id: int

    class Config:
        orm_mode = True
