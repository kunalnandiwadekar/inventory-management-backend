from fastapi import FastAPI
from app.database import engine, Base
from app.models import product
from app.routes import product as product_routes
from app.routes import supplier as supplier_routes
from app.routes import auth as auth_routes


app = FastAPI(title="Inventory Management API")

Base.metadata.create_all(bind=engine)

app.include_router(product_routes.router)
app.include_router(supplier_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Inventory Management API running"}
