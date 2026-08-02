from typing import Optional, List, TYPE_CHECKING
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from modelos.horario import Horario
    from modelos.plan_de_estudio import PlanDeEstudio


class NivelDificultad(str, Enum):
    BASICO = "BASICO"
    INTERMEDIO = "INTERMEDIO"
    AVANZADO = "AVANZADO"


class Asignatura(SQLModel, table=True):
    __tablename__ = "asignatura"

    id_asignatura: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100)
    nivel_dificultad: NivelDificultad

    horarios: List["Horario"] = Relationship(back_populates="asignatura")
    planes: List["PlanDeEstudio"] = Relationship(back_populates="asignatura")