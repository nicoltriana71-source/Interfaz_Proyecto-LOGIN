from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.base_datos import obtener_sesion
from app.modelos.asignatura import Asignatura

from app.esquemas.asignatura import (
    AsignaturaCrear,
    AsignaturaActualizar,
    AsignaturaRespuesta
)

from app.crud.asignatura import (
    crear_asignatura,
    obtener_asignaturas,
    editar_asignatura,
    eliminar_asignatura
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


@router.put("/{id_asignatura}", response_model=AsignaturaRespuesta)
def actualizar_asignatura(
    id_asignatura: int,
    datos: AsignaturaActualizar,
    sesion: Session = Depends(obtener_sesion)
):
    return editar_asignatura(sesion, id_asignatura, datos)


@router.delete("/{id_asignatura}")
def borrar_asignatura(
    id_asignatura: int,
    sesion: Session = Depends(obtener_sesion)
):
    return eliminar_asignatura(sesion, id_asignatura)