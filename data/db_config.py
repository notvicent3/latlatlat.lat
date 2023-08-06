from sqlalchemy import create_engine

# Configuración de la base de datos
DATABASE_URL = "postgresql://username:password@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)

