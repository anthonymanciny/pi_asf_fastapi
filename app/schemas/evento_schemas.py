from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class EventoBase(BaseModel):
    nome: str
    datahora: datetime
    responsavel_evento: str


class EventoCreate(EventoBase):
    pass


class EventoUpdate(BaseModel):
    nome: Optional[str]
    datahora: Optional[datetime]
    responsavel_evento: Optional[str]


class EventoResponse(EventoBase):
    id: int

    class Config:
        orm_mode = True
