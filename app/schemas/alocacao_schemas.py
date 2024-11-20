from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AlocacaoBase(BaseModel):
    id_evento: int
    id_instituicao: int
    id_espaco: int
    datahora: datetime
    status: str
    responsavel_local: str


class AlocacaoCreate(AlocacaoBase):
    pass


class AlocacaoUpdate(BaseModel):
    id_evento: Optional[int]
    id_instituicao: Optional[int]
    id_espaco: Optional[int]
    datahora: Optional[datetime]
    status: Optional[str]
    responsavel_local: Optional[str]


class AlocacaoResponse(AlocacaoBase):
    id: int

    class Config:
        orm_mode = True
