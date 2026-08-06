from sqlmodel import Session

from app.modelos.plan_de_estudio import PlanDeEstudio
from app.esquemas.plan_de_estudio import PlanDeEstudioEditar


def crear_plan(sesion: Session, plan: PlanDeEstudio):
    sesion.add(plan)
    sesion.commit()
    sesion.refresh(plan)

    return plan


def obtener_planes(sesion: Session):
    return sesion.query(PlanDeEstudio).all()


def actualizar_plan(
    sesion: Session,
    plan: PlanDeEstudio,
    datos: PlanDeEstudioEditar,
):
    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(plan, campo, valor)

    sesion.add(plan)
    sesion.commit()
    sesion.refresh(plan)

    return plan


def eliminar_plan(sesion: Session, plan: PlanDeEstudio):
    sesion.delete(plan)
    sesion.commit()

    return plan