from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from database.connection import SessionLocal, engine, Base
from passlib.context import CryptContext
from backend.models.user import User
from backend.models.product import Product 

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicialización de la aplicación y configuración de contraseñas
app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

# Modelos de solicitud y respuesta
class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str = Field(..., min_length=8, description="La contraseña debe tener al menos 8 caracteres")

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Función de ayuda para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para buscar un usuario por email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Función para crear un usuario
def create_user(db: Session, user: UserCreate):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        name=user.name,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Función para verificar la contraseña
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Ruta de registro de usuario
@app.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(db, user)
    return {"id": created_user.id, "email": created_user.email, "name": created_user.name}

# Ruta de inicio de sesión
@app.post("/login")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    print("Usuario recuperado:", db_user)
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos.")
    return {
        "message": "Inicio de sesión exitoso",
        "user_id": db_user.id,
        "email": db_user.email,
        "name": db_user.name  # Agrega el nombre del usuario a la respuesta
    }