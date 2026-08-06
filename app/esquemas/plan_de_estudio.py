from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class PlanDeEstudioCrear(SQLModel):
    id_usuario: int
    id_asignatura: int
    id_ruta: int
    titulo: str
    estado: bool
    nivel_objetivo: str


class PlanDeEstudioRespuesta(SQLModel):
    id_plan: int
    id_usuario: int
    id_asignatura: int
    id_ruta: int
    titulo: str
    fecha_creacion: datetime
    estado: bool
    nivel_objetivo: str


class PlanDeEstudioEditar(SQLModel):
    id_usuario: Optional[int] = None
    id_asignatura: Optional[int] = None
    id_ruta: Optional[int] = None
    titulo: Optional[str] = None
    estado: Optional[bool] = None
    nivel_objetivo: Optional[str] = None