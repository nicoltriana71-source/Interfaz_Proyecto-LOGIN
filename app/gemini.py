from pathlib import Path
import os

from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY en app/.env")

client = genai.Client(api_key=API_KEY)


def preguntar_ia(pregunta):
    respuesta = client.models.generate_content(
        model="gemini-flash-latest",
        contents=pregunta
    )

    return respuesta.text