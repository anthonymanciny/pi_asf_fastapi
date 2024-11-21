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

# Carregar variável de ambiente DB_URL
DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:@localhost:3306/asf_db_teste")

# Criando o engine (conexão com o banco)
engine = create_engine(DB_URL, echo=True)

# Criando uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
