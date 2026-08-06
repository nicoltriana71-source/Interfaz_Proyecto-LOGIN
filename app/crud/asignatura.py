from fastapi import HTTPException
from sqlmodel import Session

from app.modelos.asignatura import Asignatura
from app.esquemas.asignatura import AsignaturaActualizar


def crear_asignatura(sesion: Session, asignatura: Asignatura):
    sesion.add(asignatura)
    sesion.commit()
    sesion.refresh(asignatura)

    return asignatura


def obtener_asignaturas(sesion: Session):
    return sesion.query(Asignatura).all()


def editar_asignatura(
    sesion: Session,
    id_asignatura: int,
    datos: AsignaturaActualizar
):
    asignatura = sesion.get(Asignatura, id_asignatura)

    if not asignatura:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")

    asignatura.nombre = datos.nombre
    asignatura.nivel_dificultad = datos.nivel_dificultad

    sesion.add(asignatura)
    sesion.commit()
    sesion.refresh(asignatura)

    return asignatura


def eliminar_asignatura(
    sesion: Session,
    id_asignatura: int
):
    asignatura = sesion.get(Asignatura, id_asignatura)

    if not asignatura:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")

    sesion.delete(asignatura)
    sesion.commit()

    return {"mensaje": "Asignatura eliminada correctamente"}