from fastapi import FastAPI

from app.base_datos import engine
import app.modelos  
from app.rutas.usuario import router as usuarios_router

from app.rutas.asignatura import router as asignaturas_router

app = FastAPI(
    title="StudNova API"
)

app.include_router(usuarios_router)
app.include_router(asignaturas_router)


@app.get("/")
def inicio():
    return {"mensaje": "Backend funcionando"}