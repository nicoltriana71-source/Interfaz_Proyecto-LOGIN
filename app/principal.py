from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse, Response

from app.base_datos import engine
import app.modelos  # importa las 8 tablas y resuelve sus relaciones
from app.rutas.usuario import router as usuarios_router
from app.rutas.ia import router as ia_router

BASE_DIR = Path(__file__).resolve().parent.parent

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
    return RedirectResponse(url="/ia/interfaz.html")


@app.get("/ia")
@app.get("/ia/")
@app.get("/ia/interfaz.html")
def interfaz_ia_html():
    return FileResponse(BASE_DIR / "ia" / "interfaz.html")


@app.get("/ia/css.css")
def css_ia():
    return FileResponse(BASE_DIR / "ia" / "css.css")


@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)