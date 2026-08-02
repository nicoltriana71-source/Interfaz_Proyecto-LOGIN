from sqlalchemy import inspect
from base_datos import engine

inspector = inspect(engine)

tablas = inspector.get_table_names()
print(f"📋 Tablas encontradas: {tablas}\n")

for tabla in tablas:
    print(f"--- Tabla: {tabla} ---")
    columnas = inspector.get_columns(tabla)
    for col in columnas:
        pk = " (PK)" if col.get("primary_key") else ""
        print(f"  {col['name']}: {col['type']}{pk}, nullable={col['nullable']}")
    print()