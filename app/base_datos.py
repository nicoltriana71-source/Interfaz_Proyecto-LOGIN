from sqlmodel import create_engine, Session

USUARIO = "estudiante"
PASSWORD = "estudi1234"
HOST = "localhost"
PUERTO = "3306"
BASE_DATOS = "studnova"

DATABASE_URL = (
    f"mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PUERTO}/{BASE_DATOS}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def obtener_sesion():
    with Session(engine) as sesion:
        yield sesion