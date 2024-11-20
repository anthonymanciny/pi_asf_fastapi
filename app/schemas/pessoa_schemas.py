from pydantic import BaseModel
from datetime import date
from typing import Optional


class PessoaBase(BaseModel):
    nome: str
    email: Optional[str]
    telefone: Optional[str]
    cpf: str
    data_nascimento: Optional[date]
    genero: Optional[str]


class PessoaCreate(PessoaBase):
    pass


class PessoaUpdate(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    telefone: Optional[str]
    data_nascimento: Optional[date]
    genero: Optional[str]


class PessoaResponse(PessoaBase):
    id: int

    class Config:
        orm_mode = True