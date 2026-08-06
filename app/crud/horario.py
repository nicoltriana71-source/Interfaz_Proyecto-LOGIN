from sqlmodel import Session

from app.modelos.horario import Horario
from app.esquemas.horario import HorarioEditar


def crear_horario(sesion: Session, horario: Horario):
    sesion.add(horario)
    sesion.commit()
    sesion.refresh(horario)
    return horario


def obtener_horarios(sesion: Session):
    return sesion.query(Horario).all()


def actualizar_horario(
    sesion: Session,
    horario: Horario,
    datos: HorarioEditar,
):
    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(horario, campo, valor)

    sesion.add(horario)
    sesion.commit()
    sesion.refresh(horario)

    return horario


def eliminar_horario(
    sesion: Session,
    horario: Horario,
):
    sesion.delete(horario)
    sesion.commit()

    return horario