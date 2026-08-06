from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.base_datos import obtener_sesion
from app.modelos.plan_de_estudio import PlanDeEstudio
from app.esquemas.plan_de_estudio import (
    PlanDeEstudioCrear,
    PlanDeEstudioRespuesta,
    PlanDeEstudioEditar,
)
from app.crud.plan_de_estudio import (
    crear_plan,
    obtener_planes,
    actualizar_plan,
    eliminar_plan,
)

router = APIRouter(
    prefix="/planes-estudio",
    tags=["Plan de estudio"]
)


# CREAR
@router.post("/", response_model=PlanDeEstudioRespuesta)
def registrar_plan(
    datos: PlanDeEstudioCrear,
    sesion: Session = Depends(obtener_sesion),
):
    plan = PlanDeEstudio(
    id_usuario=datos.id_usuario,
    id_asignatura=datos.id_asignatura,
    id_ruta=datos.id_ruta,
    titulo=datos.titulo,
    fecha_creacion=datetime.now(),
    estado=datos.estado,
    nivel_objetivo=datos.nivel_objetivo,
)

    return crear_plan(sesion, plan)


# LISTAR
@router.get("/", response_model=list[PlanDeEstudioRespuesta])
def listar_planes(
    sesion: Session = Depends(obtener_sesion),
):
    return obtener_planes(sesion)


# EDITAR
@router.put("/{id_plan}", response_model=PlanDeEstudioRespuesta)
def editar_plan(
    id_plan: int,
    datos: PlanDeEstudioEditar,
    sesion: Session = Depends(obtener_sesion),
):
    plan = sesion.get(PlanDeEstudio, id_plan)

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plan de estudio no encontrado",
        )

    return actualizar_plan(sesion, plan, datos)


# ELIMINAR
@router.delete("/{id_plan}")
def eliminar_plan_estudio(
    id_plan: int,
    sesion: Session = Depends(obtener_sesion),
):
    plan = sesion.get(PlanDeEstudio, id_plan)

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plan de estudio no encontrado",
        )

    eliminar_plan(sesion, plan)

    return {"mensaje": "Plan de estudio eliminado correctamente"}