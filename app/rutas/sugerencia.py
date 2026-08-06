from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.base_datos import obtener_sesion
from app.modelos.sugerencia import Sugerencia

from app.esquemas.sugerencia import (
    SugerenciaCrear,
    SugerenciaRespuesta,
    SugerenciaEditar,
)

from app.crud.sugerencia import (
    crear_sugerencia,
    obtener_sugerencias,
    actualizar_sugerencia,
    eliminar_sugerencia,
)

router = APIRouter(
    prefix="/sugerencias",
    tags=["Sugerencias"]
)


@router.post("/", response_model=SugerenciaRespuesta)
def registrar_sugerencia(
    datos: SugerenciaCrear,
    sesion: Session = Depends(obtener_sesion),
):
    sugerencia = Sugerencia(
        id_plan=datos.id_plan,
        titulo=datos.titulo,
        descripcion=datos.descripcion,
        tipo=datos.tipo,
    )

    return crear_sugerencia(sesion, sugerencia)


@router.get("/", response_model=list[SugerenciaRespuesta])
def listar_sugerencias(
    sesion: Session = Depends(obtener_sesion),
):
    return obtener_sugerencias(sesion)


@router.get("/{id_sugerencia}", response_model=SugerenciaRespuesta)
def obtener_sugerencia(
    id_sugerencia: int,
    sesion: Session = Depends(obtener_sesion),
):
    sugerencia = sesion.get(Sugerencia, id_sugerencia)

    if not sugerencia:
        raise HTTPException(
            status_code=404,
            detail="Sugerencia no encontrada",
        )

    return sugerencia


@router.put("/{id_sugerencia}", response_model=SugerenciaRespuesta)
def editar_sugerencia(
    id_sugerencia: int,
    datos: SugerenciaEditar,
    sesion: Session = Depends(obtener_sesion),
):
    sugerencia = sesion.get(Sugerencia, id_sugerencia)

    if not sugerencia:
        raise HTTPException(
            status_code=404,
            detail="Sugerencia no encontrada",
        )

    return actualizar_sugerencia(
        sesion,
        sugerencia,
        datos,
    )


@router.delete("/{id_sugerencia}")
def eliminar_sugerencia_endpoint(
    id_sugerencia: int,
    sesion: Session = Depends(obtener_sesion),
):
    sugerencia = sesion.get(Sugerencia, id_sugerencia)

    if not sugerencia:
        raise HTTPException(
            status_code=404,
            detail="Sugerencia no encontrada",
        )

    eliminar_sugerencia(
        sesion,
        sugerencia,
    )

    return {
        "mensaje": "Sugerencia eliminada correctamente"
    }