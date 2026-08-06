from typing import Optional
from sqlmodel import SQLModel


class HorarioCrear(SQLModel):
    id_asignatura: int
    dia_semana: int


class HorarioRespuesta(SQLModel):
    id_horario: int
    id_asignatura: int
    dia_semana: int


class HorarioEditar(SQLModel):
    id_asignatura: Optional[int] = None
    dia_semana: Optional[int] = None