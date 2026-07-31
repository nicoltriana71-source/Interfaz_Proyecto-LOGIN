from sqlmodel import Session

from app.modelos.usuario import Usuario


def crear_usuario(sesion: Session, usuario: Usuario):

    sesion.add(usuario)
    sesion.commit()
    sesion.refresh(usuario)

    return usuario