from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.base_datos import obtener_sesion
from app.modelos.sesion_de_estudio import SesionDeEstudio

from app.esquemas.sesion_de_estudio import (
    SesionDeEstudioCrear,
    SesionDeEstudioRespuesta,
    SesionDeEstudioEditar,
)

from app.crud.sesion_de_estudio import (
    crear_sesion,
    obtener_sesiones,
    actualizar_sesion,
    eliminar_sesion,
)

router = APIRouter(
    prefix="/sesiones-estudio",
    tags=["Sesiones de estudio"]
)


@router.post("/", response_model=SesionDeEstudioRespuesta)
def registrar_sesion(
    datos: SesionDeEstudioCrear,
    sesion: Session = Depends(obtener_sesion),
):
    nueva_sesion = SesionDeEstudio(
        id_usuario=datos.id_usuario,
        fecha=datos.fecha,
        tiempo_limite=datos.tiempo_limite,
        tiempo_utilizado=datos.tiempo_utilizado,
        fatiga_detectada=datos.fatiga_detectada,
    )

    return crear_sesion(sesion, nueva_sesion)


@router.get("/", response_model=list[SesionDeEstudioRespuesta])
def listar_sesiones(
    sesion: Session = Depends(obtener_sesion),
):
    return obtener_sesiones(sesion)


@router.get("/{id_sesion}", response_model=SesionDeEstudioRespuesta)
def obtener_sesion_por_id(
    id_sesion: int,
    sesion: Session = Depends(obtener_sesion),
):
    sesion_estudio = sesion.get(SesionDeEstudio, id_sesion)

    if not sesion_estudio:
        raise HTTPException(
            status_code=404,
            detail="Sesión de estudio no encontrada",
        )

    return sesion_estudio


@router.put("/{id_sesion}", response_model=SesionDeEstudioRespuesta)
def editar_sesion(
    id_sesion: int,
    datos: SesionDeEstudioEditar,
    sesion: Session = Depends(obtener_sesion),
):
    sesion_estudio = sesion.get(SesionDeEstudio, id_sesion)

    if not sesion_estudio:
        raise HTTPException(
            status_code=404,
            detail="Sesión de estudio no encontrada",
        )

    return actualizar_sesion(
        sesion,
        sesion_estudio,
        datos,
    )


@router.delete("/{id_sesion}")
def eliminar_sesion_endpoint(
    id_sesion: int,
    sesion: Session = Depends(obtener_sesion),
):
    sesion_estudio = sesion.get(SesionDeEstudio, id_sesion)

    if not sesion_estudio:
        raise HTTPException(
            status_code=404,
            detail="Sesión de estudio no encontrada",
        )

    eliminar_sesion(
        sesion,
        sesion_estudio,
    )

    return {
        "mensaje": "Sesión de estudio eliminada correctamente"
    }