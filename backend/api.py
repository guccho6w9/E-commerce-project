from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.connection import SessionLocal, engine, Base  # Cambiar a la ruta correcta
from backend.models.product import Product  # Asegúrate de la ruta correcta

# Asegúrate de que tus tablas estén creadas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Define el modelo del producto para la API
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image_url: str | None = None

# Ruta para crear un nuevo producto
@app.post("/products/")
async def create_product(product: ProductCreate):
    db: Session = SessionLocal()
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        image_url=product.image_url
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
