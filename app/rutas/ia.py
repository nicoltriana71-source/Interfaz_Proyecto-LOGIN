from fastapi import APIRouter
from pydantic import BaseModel

from app.gemini import preguntar_ia

router = APIRouter(
    prefix="/ia",
    tags=["IA"]
)

class Mensaje(BaseModel):
    mensaje: str


@router.post("/chat")
def chat(datos: Mensaje):
    respuesta = preguntar_ia(datos.mensaje)

    return {
        "respuesta": respuesta
    }