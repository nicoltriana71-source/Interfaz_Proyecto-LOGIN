from sqlmodel import Session

from app.modelos.sesion_de_estudio import SesionDeEstudio
from app.esquemas.sesion_de_estudio import SesionDeEstudioEditar


def crear_sesion(sesion: Session, nueva_sesion: SesionDeEstudio):
    sesion.add(nueva_sesion)
    sesion.commit()
    sesion.refresh(nueva_sesion)

    return nueva_sesion


def obtener_sesiones(sesion: Session):
    return sesion.query(SesionDeEstudio).all()


def actualizar_sesion(
    sesion: Session,
    sesion_estudio: SesionDeEstudio,
    datos: SesionDeEstudioEditar,
):
    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(sesion_estudio, campo, valor)

    sesion.add(sesion_estudio)
    sesion.commit()
    sesion.refresh(sesion_estudio)

    return sesion_estudio


def eliminar_sesion(
    sesion: Session,
    sesion_estudio: SesionDeEstudio,
):
    sesion.delete(sesion_estudio)
    sesion.commit()

    return sesion_estudio