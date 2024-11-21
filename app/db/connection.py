# from decouple import config
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# DB_URL = config('DB_URL')


# engine = create_engine(DB_URL, pool_pre_ping=True)
# SessionLocal=sessionmaker(bind=engine)




# connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Carregar a URL do banco de dados da variável de ambiente DB_URL
DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:@localhost:3306/asf_db_teste")
print("Banco Utilizado é", DB_URL)

# Criando o engine (conexão com o banco)
engine = create_engine(DB_URL, echo=True)

# Criando uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
