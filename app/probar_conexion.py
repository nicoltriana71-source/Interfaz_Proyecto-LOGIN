from base_datos import engine
from sqlmodel import Session, text

try:
    with Session(engine) as sesion:
        resultado = sesion.exec(text("SELECT 1"))
        print("✅ Conexión exitosa:", resultado.first())
except Exception as e:
    print("❌ Error de conexión:", e)