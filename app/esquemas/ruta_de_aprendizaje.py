from typing import Optional
from sqlmodel import SQLModel

from app.modelos.ruta_de_aprendizaje import NivelRuta


class RutaDeAprendizajeCrear(SQLModel):
    nivel: NivelRuta
    tema: str
    descripcion: str
    orden: int


class RutaDeAprendizajeRespuesta(SQLModel):
    id_ruta: int
    nivel: NivelRuta
    tema: str
    descripcion: str
    orden: int


class RutaDeAprendizajeEditar(SQLModel):
    nivel: Optional[NivelRuta] = None
    tema: Optional[str] = None
    descripcion: Optional[str] = None
    orden: Optional[int] = None