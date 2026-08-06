from sqlmodel import Session

from app.modelos.ruta_de_aprendizaje import RutaDeAprendizaje
from app.esquemas.ruta_de_aprendizaje import RutaDeAprendizajeEditar


def crear_ruta(sesion: Session, ruta: RutaDeAprendizaje):
    sesion.add(ruta)
    sesion.commit()
    sesion.refresh(ruta)

    return ruta


def obtener_rutas(sesion: Session):
    return sesion.query(RutaDeAprendizaje).all()


def actualizar_ruta(
    sesion: Session,
    ruta: RutaDeAprendizaje,
    datos: RutaDeAprendizajeEditar,
):
    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(ruta, campo, valor)

    sesion.add(ruta)
    sesion.commit()
    sesion.refresh(ruta)

    return ruta


def eliminar_ruta(
    sesion: Session,
    ruta: RutaDeAprendizaje,
):
    sesion.delete(ruta)
    sesion.commit()

    return ruta