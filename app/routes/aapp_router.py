from fastapi import APIRouter
from app.routes.pessoa_router import pessoa_router
from app.routes.alocacao_router import alocacao_router
from app.routes.instituicao_router import instituticao_router

# Criação de um roteador principal
api_router = APIRouter()

# Registro das rotas no roteador principal
api_router.include_router(pessoa_router)
api_router.include_router(alocacao_router)
api_router.include_router(instituticao_router)