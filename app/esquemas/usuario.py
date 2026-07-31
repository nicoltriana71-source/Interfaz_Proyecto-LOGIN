from sqlmodel import SQLModel


class UsuarioCrear(SQLModel):
    nombre: str
    correo: str
    contraseña: str
    rol: str


class UsuarioRespuesta(SQLModel):
    id_usuario: int
    nombre: str
    correo: str
    rol: str