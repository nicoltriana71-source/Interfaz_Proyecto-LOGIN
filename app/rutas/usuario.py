from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.base_datos import obtener_sesion
from app.modelos.usuario import Usuario
from app.esquemas.usuario import UsuarioCrear
from app.crud.usuario import crear_usuario

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