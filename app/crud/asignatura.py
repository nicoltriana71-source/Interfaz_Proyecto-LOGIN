from sqlmodel import Session

from app.modelos.asignatura import Asignatura


def crear_asignatura(sesion: Session, asignatura: Asignatura):

    sesion.add(asignatura)
    sesion.commit()
    sesion.refresh(asignatura)

    return asignatura


def obtener_asignaturas(sesion: Session):

    return sesion.query(Asignatura).all()