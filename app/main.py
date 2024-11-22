from fastapi import FastAPI
from app.routes.aapp_router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Lista de origens permitidas (onde o frontend pode estar hospedado)
origins = [
    "http://localhost:3000",  # React ou outro frontend local
    "https://meu-frontend.com",  # Frontend em produção
]

# Adicionando o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Origem permitida
    allow_credentials=True,  # Permitir envio de cookies e credenciais
    allow_methods=["*"],  # Métodos HTTP permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Cabeçalhos permitidos nas requisições
)


@app.get('/')
def root():
    return "ok"

app.include_router(api_router)

