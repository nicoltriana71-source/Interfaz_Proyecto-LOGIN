from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.base_datos import obtener_sesion
from app.modelos.chat_ia import ChatIA

from app.esquemas.chat_ia import (
    ChatIACrear,
    ChatIARespuesta,
    ChatIAEditar,
)

from app.crud.chat_ia import (
    crear_chat,
    obtener_chats,
    actualizar_chat,
    eliminar_chat,
)

router = APIRouter(
    prefix="/chat-ia",
    tags=["Chat IA"]
)


@router.post("/", response_model=ChatIARespuesta)
def registrar_chat(
    datos: ChatIACrear,
    sesion: Session = Depends(obtener_sesion),
):
    chat = ChatIA(
        id_usuario=datos.id_usuario,
        pregunta=datos.pregunta,
        respuesta=datos.respuesta,
        fecha=datos.fecha,
    )

    return crear_chat(sesion, chat)


@router.get("/", response_model=list[ChatIARespuesta])
def listar_chats(
    sesion: Session = Depends(obtener_sesion),
):
    return obtener_chats(sesion)


@router.get("/{id_chat}", response_model=ChatIARespuesta)
def obtener_chat(
    id_chat: int,
    sesion: Session = Depends(obtener_sesion),
):
    chat = sesion.get(ChatIA, id_chat)

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat no encontrado",
        )

    return chat


@router.put("/{id_chat}", response_model=ChatIARespuesta)
def editar_chat(
    id_chat: int,
    datos: ChatIAEditar,
    sesion: Session = Depends(obtener_sesion),
):
    chat = sesion.get(ChatIA, id_chat)

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat no encontrado",
        )

    return actualizar_chat(
        sesion,
        chat,
        datos,
    )


@router.delete("/{id_chat}")
def eliminar_chat_endpoint(
    id_chat: int,
    sesion: Session = Depends(obtener_sesion),
):
    chat = sesion.get(ChatIA, id_chat)

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat no encontrado",
        )

    eliminar_chat(
        sesion,
        chat,
    )

    return {
        "mensaje": "Chat eliminado correctamente"
    }