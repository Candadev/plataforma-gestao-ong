import enum

from sqlalchemy import Boolean, Column, Enum, Integer, String

from app.database.database import Base


class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    AUDITOR = "AUDITOR"
    PARCEIRO = "PARCEIRO"
    PUBLICO = "PUBLICO"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    perfil = Column(Enum(RoleEnum), default=RoleEnum.PUBLICO, nullable=False)
    ativo = Column(Boolean, default=True)
