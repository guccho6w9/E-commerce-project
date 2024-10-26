import sys
import os

# Obtener la ruta al directorio raíz del proyecto
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

# Agregar el directorio raíz al sys.path


from database.connection import Base, engine
from backend.models.product import Product
from backend.models.user import User

# Crear las tablas
Base.metadata.create_all(bind=engine)
