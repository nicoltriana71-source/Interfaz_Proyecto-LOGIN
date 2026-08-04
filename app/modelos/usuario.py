from typing import Optional, List, TYPE_CHECKING
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from modelos.chat_ia import ChatIA
    from modelos.plan_de_estudio import PlanDeEstudio
    from modelos.sesion_de_estudio import SesionDeEstudio


class RolUsuario(str, Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    ESTUDIANTE = "ESTUDIANTE"


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id_usuario: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100)
    correo: str = Field(max_length=100)
    contraseña: str = Field(max_length=100)
    rol: RolUsuario

    chats: List["ChatIA"] = Relationship(back_populates="usuario")
    planes: List["PlanDeEstudio"] = Relationship(back_populates="usuario")
    sesiones: List["SesionDeEstudio"] = Relationship(back_populates="usuario")