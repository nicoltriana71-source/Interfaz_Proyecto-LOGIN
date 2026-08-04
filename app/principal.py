from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.base_datos import engine
import app.modelos  # importa las 8 tablas y resuelve sus relaciones
from app.rutas.usuario import router as usuarios_router
from app.rutas.ia import router as ia_router

app = FastAPI(
    title="StudNova API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router)
app.include_router(ia_router)


@app.get("/")
def inicio():
    return {"mensaje": "Backend funcionando"}