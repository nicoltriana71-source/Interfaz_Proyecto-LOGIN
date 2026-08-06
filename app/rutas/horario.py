from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.base_datos import obtener_sesion

from app.modelos.horario import Horario

from app.esquemas.horario import (
    HorarioCrear,
    HorarioRespuesta,
    HorarioEditar,
)

from app.crud.horario import (
    crear_horario,
    obtener_horarios,
    actualizar_horario,
    eliminar_horario,
)

router = APIRouter(
    prefix="/horarios",
    tags=["Horario"]
)


@router.post("/", response_model=HorarioRespuesta)
def registrar_horario(
    datos: HorarioCrear,
    sesion: Session = Depends(obtener_sesion),
):

    horario = Horario(
        id_asignatura=datos.id_asignatura,
        dia_semana=datos.dia_semana,
    )

    return crear_horario(sesion, horario)


@router.get("/", response_model=list[HorarioRespuesta])
def listar_horarios(
    sesion: Session = Depends(obtener_sesion),
):
    return obtener_horarios(sesion)


@router.get("/{id_horario}", response_model=HorarioRespuesta)
def obtener_horario(
    id_horario: int,
    sesion: Session = Depends(obtener_sesion),
):

    horario = sesion.get(Horario, id_horario)

    if not horario:
        raise HTTPException(
            status_code=404,
            detail="Horario no encontrado",
        )

    return horario


@router.put("/{id_horario}", response_model=HorarioRespuesta)
def editar_horario(
    id_horario: int,
    datos: HorarioEditar,
    sesion: Session = Depends(obtener_sesion),
):

    horario = sesion.get(Horario, id_horario)

    if not horario:
        raise HTTPException(
            status_code=404,
            detail="Horario no encontrado",
        )

    return actualizar_horario(
        sesion,
        horario,
        datos,
    )


@router.delete("/{id_horario}")
def eliminar_horario_endpoint(
    id_horario: int,
    sesion: Session = Depends(obtener_sesion),
):

    horario = sesion.get(Horario, id_horario)

    if not horario:
        raise HTTPException(
            status_code=404,
            detail="Horario no encontrado",
        )

    eliminar_horario(
        sesion,
        horario,
    )

    return {
        "mensaje": "Horario eliminado correctamente"
    }