from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.base_datos import obtener_sesion

from app.modelos.ruta_de_aprendizaje import RutaDeAprendizaje

from app.esquemas.ruta_de_aprendizaje import (
    RutaDeAprendizajeCrear,
    RutaDeAprendizajeRespuesta,
    RutaDeAprendizajeEditar,
)

from app.crud.ruta_de_aprendizaje import (
    crear_ruta,
    obtener_rutas,
    actualizar_ruta,
    eliminar_ruta,
)

router = APIRouter(
    prefix="/rutas-aprendizaje",
    tags=["Ruta de aprendizaje"]
)


@router.post("/", response_model=RutaDeAprendizajeRespuesta)
def registrar_ruta(
    datos: RutaDeAprendizajeCrear,
    sesion: Session = Depends(obtener_sesion),
):

    ruta = RutaDeAprendizaje(
        nivel=datos.nivel,
        tema=datos.tema,
        descripcion=datos.descripcion,
        orden=datos.orden,
    )

    return crear_ruta(sesion, ruta)


@router.get("/", response_model=list[RutaDeAprendizajeRespuesta])
def listar_rutas(
    sesion: Session = Depends(obtener_sesion),
):
    return obtener_rutas(sesion)


@router.get("/{id_ruta}", response_model=RutaDeAprendizajeRespuesta)
def obtener_ruta(
    id_ruta: int,
    sesion: Session = Depends(obtener_sesion),
):

    ruta = sesion.get(RutaDeAprendizaje, id_ruta)

    if not ruta:
        raise HTTPException(
            status_code=404,
            detail="Ruta de aprendizaje no encontrada",
        )

    return ruta


@router.put("/{id_ruta}", response_model=RutaDeAprendizajeRespuesta)
def editar_ruta(
    id_ruta: int,
    datos: RutaDeAprendizajeEditar,
    sesion: Session = Depends(obtener_sesion),
):

    ruta = sesion.get(RutaDeAprendizaje, id_ruta)

    if not ruta:
        raise HTTPException(
            status_code=404,
            detail="Ruta de aprendizaje no encontrada",
        )

    return actualizar_ruta(
        sesion,
        ruta,
        datos,
    )


@router.delete("/{id_ruta}")
def eliminar_ruta_endpoint(
    id_ruta: int,
    sesion: Session = Depends(obtener_sesion),
):

    ruta = sesion.get(RutaDeAprendizaje, id_ruta)

    if not ruta:
        raise HTTPException(
            status_code=404,
            detail="Ruta de aprendizaje no encontrada",
        )

    eliminar_ruta(
        sesion,
        ruta,
    )

    return {
        "mensaje": "Ruta de aprendizaje eliminada correctamente"
    }