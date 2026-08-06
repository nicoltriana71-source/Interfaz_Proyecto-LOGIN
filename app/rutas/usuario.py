from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.base_datos import obtener_sesion
from app.modelos.usuario import Usuario
from app.esquemas.usuario import UsuarioCrear, UsuarioActualizar
from app.crud.usuario import (
    crear_usuario,
    editar_usuario,
    eliminar_usuario
)
from app.crud.usuario import (
    crear_usuario,
    editar_usuario,
    eliminar_usuario,
    listar_usuarios
)

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.post("/")
def registrar_usuario(
    datos: UsuarioCrear,
    sesion: Session = Depends(obtener_sesion)
):
    usuario = Usuario(
        nombre=datos.nombre,
        correo=datos.correo,
        contraseña=datos.contraseña,
        rol=datos.rol
    )

    return crear_usuario(sesion, usuario)

@router.get("/")
def obtener_usuarios(
    sesion: Session = Depends(obtener_sesion)
):
    return listar_usuarios(sesion)

@router.put("/{id_usuario}")
def actualizar_usuario(
    id_usuario: int,
    datos: UsuarioActualizar,
    sesion: Session = Depends(obtener_sesion)
):
    return editar_usuario(sesion, id_usuario, datos)


@router.delete("/{id_usuario}")
def borrar_usuario(
    id_usuario: int,
    sesion: Session = Depends(obtener_sesion)
):
    return eliminar_usuario(sesion, id_usuario)