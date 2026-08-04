from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.base_datos import obtener_sesion

from app.modelos.asignatura import Asignatura

from app.esquemas.asignatura import (
    AsignaturaCrear,
    AsignaturaRespuesta
)

from app.crud.asignatura import (
    crear_asignatura,
    obtener_asignaturas
)

router = APIRouter(
    prefix="/asignaturas",
    tags=["Asignaturas"]
)


@router.post("/", response_model=AsignaturaRespuesta)
def registrar_asignatura(
    datos: AsignaturaCrear,
    sesion: Session = Depends(obtener_sesion)
):

    asignatura = Asignatura(
        nombre=datos.nombre,
        nivel_dificultad=datos.nivel_dificultad
    )

    return crear_asignatura(sesion, asignatura)


@router.get("/", response_model=list[AsignaturaRespuesta])
def listar_asignaturas(
    sesion: Session = Depends(obtener_sesion)
):

    return obtener_asignaturas(sesion)