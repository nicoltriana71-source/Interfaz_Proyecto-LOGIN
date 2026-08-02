from fastapi import FastAPI

from app.base_datos import engine
import app.modelos  # importa las 8 tablas y resuelve sus relaciones
from app.rutas.usuario import router as usuarios_router

app = FastAPI(
    title="StudNova API"
)

app.include_router(usuarios_router)


@app.get("/")
def inicio():
    return {"mensaje": "Backend funcionando"}