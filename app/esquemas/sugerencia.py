from typing import Optional
from sqlmodel import SQLModel

from app.modelos.sugerencia import TipoSugerencia


class SugerenciaCrear(SQLModel):
    id_plan: int
    titulo: str
    descripcion: str
    tipo: TipoSugerencia


class SugerenciaRespuesta(SQLModel):
    id_sugerencia: int
    id_plan: int
    titulo: str
    descripcion: str
    tipo: TipoSugerencia


class SugerenciaEditar(SQLModel):
    id_plan: Optional[int] = None
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    tipo: Optional[TipoSugerencia] = None