from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel


class ChatIACrear(SQLModel):
    id_usuario: int
    pregunta: str
    respuesta: str
    fecha: datetime


class ChatIARespuesta(SQLModel):
    id_chat: int
    id_usuario: int
    pregunta: str
    respuesta: str
    fecha: datetime


class ChatIAEditar(SQLModel):
    id_usuario: Optional[int] = None
    pregunta: Optional[str] = None
    respuesta: Optional[str] = None
    fecha: Optional[datetime] = None