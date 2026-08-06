from sqlmodel import SQLModel
from app.modelos.asignatura import NivelDificultad


class AsignaturaCrear(SQLModel):
    nombre: str
    nivel_dificultad: NivelDificultad


class AsignaturaActualizar(SQLModel):
    nombre: str
    nivel_dificultad: NivelDificultad


class AsignaturaRespuesta(SQLModel):
    id_asignatura: int
    nombre: str
    nivel_dificultad: NivelDificultad