from fastapi import HTTPException
from sqlmodel import Session

from app.modelos.usuario import Usuario
from app.esquemas.usuario import UsuarioActualizar
from sqlmodel import Session, select


def crear_usuario(sesion: Session, usuario: Usuario):
    sesion.add(usuario)
    sesion.commit()
    sesion.refresh(usuario)

    return usuario


def editar_usuario(
    sesion: Session,
    id_usuario: int,
    datos: UsuarioActualizar
):
    usuario = sesion.get(Usuario, id_usuario)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.nombre = datos.nombre
    usuario.correo = datos.correo
    usuario.contraseña = datos.contraseña
    usuario.rol = datos.rol

    sesion.add(usuario)
    sesion.commit()
    sesion.refresh(usuario)

    return usuario


def eliminar_usuario(
    sesion: Session,
    id_usuario: int
):
    usuario = sesion.get(Usuario, id_usuario)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    sesion.delete(usuario)
    sesion.commit()

    return {"mensaje": "Usuario eliminado correctamente"}

def listar_usuarios(sesion: Session):
    return sesion.exec(select(Usuario)).all()