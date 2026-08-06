from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel


class SesionDeEstudioCrear(SQLModel):
    id_usuario: int
    fecha: datetime
    tiempo_limite: int
    tiempo_utilizado: int
    fatiga_detectada: bool


class SesionDeEstudioRespuesta(SQLModel):
    id_sesion: int
    id_usuario: int
    fecha: datetime
    tiempo_limite: int
    tiempo_utilizado: int
    fatiga_detectada: bool


class SesionDeEstudioEditar(SQLModel):
    id_usuario: Optional[int] = None
    fecha: Optional[datetime] = None
    tiempo_limite: Optional[int] = None
    tiempo_utilizado: Optional[int] = None
    fatiga_detectada: Optional[bool] = None