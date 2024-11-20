from pydantic import BaseModel
from typing import Optional


class EspacoInstituicaoBase(BaseModel):
    id_instituicao: int
    nome: str
    capacidade: int
    responsavel: str


class EspacoInstituicaoCreate(EspacoInstituicaoBase):
    pass


class EspacoInstituicaoUpdate(BaseModel):
    id_instituicao: Optional[int]
    nome: Optional[str]
    capacidade: Optional[int]
    responsavel: Optional[str]


class EspacoInstituicaoResponse(EspacoInstituicaoBase):
    id: int

    class Config:
        orm_mode = True
