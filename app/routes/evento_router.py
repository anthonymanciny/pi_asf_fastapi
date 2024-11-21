from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.evento_service import EventoService
from app.schemas.evento_schemas import EventoCreate, EventoUpdate, EventoResponse
from app.db.depends import get_db

evento_router = APIRouter(prefix="/eventos", tags=["Eventos"])

@evento_router.post("/", response_model=EventoResponse)
def create_evento(evento_data: EventoCreate, db: Session = Depends(get_db)):
    evento = EventoService(db)
    return evento.create_evento(evento_data)


@evento_router.get("/{evento_id}", response_model=EventoResponse)
def get_evento(evento_id: int, db: Session = Depends(get_db)):
    evento = EventoService(db)
    evento = evento.get_evento(evento_id)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado")
    return evento


@evento_router.put("/{evento_id}", response_model=EventoResponse)
def update_evento(evento_id: int, evento_data: EventoUpdate, db: Session = Depends(get_db)):
    evento = EventoService(db)
    evento = evento.update_evento(evento_id, evento_data)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado")
    return evento


@evento_router.delete("/{evento_id}", response_model=dict)
def delete_evento(evento_id: int, db: Session = Depends(get_db)):
    evento = EventoService(db)
    evento = evento.delete_evento(evento_id)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado")
    return {"message": "Evento deletado com sucesso"}


@evento_router.get("/", response_model=list[EventoResponse])
def list_eventos(db: Session = Depends(get_db)):
    evento = EventoService(db)
    return evento.list_eventos()
