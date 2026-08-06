from sqlmodel import Session

from app.modelos.sugerencia import Sugerencia
from app.esquemas.sugerencia import SugerenciaEditar


def crear_sugerencia(sesion: Session, sugerencia: Sugerencia):
    sesion.add(sugerencia)
    sesion.commit()
    sesion.refresh(sugerencia)

    return sugerencia


def obtener_sugerencias(sesion: Session):
    return sesion.query(Sugerencia).all()


def actualizar_sugerencia(
    sesion: Session,
    sugerencia: Sugerencia,
    datos: SugerenciaEditar,
):
    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(sugerencia, campo, valor)

    sesion.add(sugerencia)
    sesion.commit()
    sesion.refresh(sugerencia)

    return sugerencia


def eliminar_sugerencia(
    sesion: Session,
    sugerencia: Sugerencia,
):
    sesion.delete(sugerencia)
    sesion.commit()

    return sugerencia