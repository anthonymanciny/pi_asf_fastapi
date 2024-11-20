from pydantic import BaseModel
from typing import Optional


class InstituicaoBase(BaseModel):
    nome: str
    email: str
    endereco: str
    telefone: str
    observacao: Optional[str] = None


class InstituicaoCreate(InstituicaoBase):
    pass


class InstituicaoUpdate(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    endereco: Optional[str]
    telefone: Optional[str]
    observacao: Optional[str]


class InstituicaoResponse(InstituicaoBase):
    id: int

    class Config:
        orm_mode = True
