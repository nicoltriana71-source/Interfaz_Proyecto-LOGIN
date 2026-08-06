from sqlmodel import Session

from app.modelos.chat_ia import ChatIA
from app.esquemas.chat_ia import ChatIAEditar


def crear_chat(sesion: Session, chat: ChatIA):
    sesion.add(chat)
    sesion.commit()
    sesion.refresh(chat)

    return chat


def obtener_chats(sesion: Session):
    return sesion.query(ChatIA).all()


def actualizar_chat(
    sesion: Session,
    chat: ChatIA,
    datos: ChatIAEditar,
):
    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(chat, campo, valor)

    sesion.add(chat)
    sesion.commit()
    sesion.refresh(chat)

    return chat


def eliminar_chat(
    sesion: Session,
    chat: ChatIA,
):
    sesion.delete(chat)
    sesion.commit()

    return chat