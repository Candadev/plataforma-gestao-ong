import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# A URL do banco vem da variável de ambiente DATABASE_URL.
# Sem ela, usa SQLite local (ideal para desenvolvimento).
# Para PostgreSQL: postgresql://usuario:senha@servidor:5432/nome_do_banco
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./amad.db")

# Alguns provedores entregam "postgres://", que o SQLAlchemy não aceita.
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
        "postgres://", "postgresql://", 1
    )

# O argumento check_same_thread só existe no SQLite.
connect_args = {}
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Abre uma sessão do banco para cada requisição e a fecha no final."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
