from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.espacoinstituicao_service import EspacoInstituicaoService
from app.schemas.espacaoinstituicao_schemas import EspacoInstituicaoCreate, EspacoInstituicaoUpdate, EspacoInstituicaoResponse
from app.db.depends import get_db

espaco_instituicao_router = APIRouter(prefix="/espacos", tags=["Espaços Institucionais"])

@espaco_instituicao_router.post("/", response_model=EspacoInstituicaoResponse)
def create_espaco(espaco_data: EspacoInstituicaoCreate, get_db: Session = Depends(get_db)):
    espaco = EspacoInstituicaoService.create(get_db, espaco_data)
    return espaco

@espaco_instituicao_router.get("/{espaco_id}", response_model=EspacoInstituicaoResponse)
def get_espaco(espaco_id: int, get_db: Session = Depends(get_db)):
    espaco = EspacoInstituicaoService.get(get_db, espaco_id)
    if not espaco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espaço Institucional não encontrado")
    return espaco

@espaco_instituicao_router.put("/{espaco_id}", response_model=EspacoInstituicaoResponse)
def update_espaco(espaco_id: int, espaco_data: EspacoInstituicaoUpdate, get_db: Session = Depends(get_db)):
    espaco = EspacoInstituicaoService.update(get_db, espaco_id, espaco_data)
    if not espaco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espaço Institucional não encontrado")
    return espaco

@espaco_instituicao_router.delete("/{espaco_id}", response_model=dict)
def delete_espaco(espaco_id: int, get_db: Session = Depends(get_db)):
    espaco = EspacoInstituicaoService.delete(get_db, espaco_id)
    if not espaco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espaço Institucional não encontrado")
    return {"message": "Espaço Institucional deletado com sucesso"}

@espaco_instituicao_router.get("/", response_model=list[EspacoInstituicaoResponse])
def list_espacos(get_db: Session = Depends(get_db)):
    espacos = EspacoInstituicaoService.get_all(get_db)
    return espacos
