import os
from dotenv import load_dotenv  # Importar load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter os valores das variáveis de ambiente
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD", "")  # Se a senha estiver vazia
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Construir a URL de conexão com o banco de dados
DB_URL = f"mysql+pymysql://{USER}:{PASSWORD}@localhost:3306/{DATABASE_NAME}"

# Verificar se a URL foi formada corretamente
print("Banco de dados URL:", DB_URL)

# Criando o engine (conexão com o banco)
engine = create_engine(DB_URL, echo=True)

# Criando uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
