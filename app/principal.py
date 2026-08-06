from fastapi import FastAPI

from app.base_datos import engine
import app.modelos  
from app.rutas.usuario import router as usuarios_router

from app.rutas.asignatura import router as asignaturas_router
from app.rutas.plan_de_estudio import router as planes_router 
from app.rutas.horario import router as horarios_router
from app.rutas.ruta_de_aprendizaje import router as rutas_aprendizaje_router
from app.rutas.sesion_de_estudio import router as sesiones_router
from app.rutas.sugerencia import router as sugerencias_router
from app.rutas.chat_ia import router as chat_ia_router

app = FastAPI(
    title="StudNova API"
)

app.include_router(usuarios_router)
app.include_router(asignaturas_router)
app.include_router(planes_router)
app.include_router(horarios_router)
app.include_router(rutas_aprendizaje_router)
app.include_router(sesiones_router)
app.include_router(sugerencias_router)
app.include_router(chat_ia_router)


@app.get("/")
def inicio():
    return {"mensaje": "Backend funcionando"}