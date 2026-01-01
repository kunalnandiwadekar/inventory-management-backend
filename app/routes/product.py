from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductOut
from app.schemas.stock import StockUpdate
from app.deps import get_db

router = APIRouter(prefix="/products", tags=["Products"])


# ----------------------------
# CREATE PRODUCT
# ----------------------------
@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        product_name=product.name,
        category=product.category,
        unit=product.unit,
        price=product.price,
        min_stock=product.min_stock,
        current_stock=product.current_stock,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# ----------------------------
# GET ALL PRODUCTS
# ----------------------------
@router.get("/", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


# ----------------------------
# GET SINGLE PRODUCT
# ----------------------------
@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(
        Product.product_id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# ----------------------------
# UPDATE PRODUCT
# ----------------------------
@router.put("/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    updated: ProductCreate,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.product_id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


# ----------------------------
# DELETE PRODUCT
# ----------------------------
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(
        Product.product_id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}


# ----------------------------
# STOCK IN
# ----------------------------
@router.post("/{product_id}/stock-in")
def stock_in(
    product_id: int,
    data: StockUpdate,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.product_id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.current_stock += data.quantity
    db.commit()
    db.refresh(product)

    return {
        "message": "Stock added successfully",
        "current_stock": product.current_stock
    }


# ----------------------------
# STOCK OUT
# ----------------------------
@router.post("/{product_id}/stock-out")
def stock_out(
    product_id: int,
    data: StockUpdate,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.product_id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.current_stock < data.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    product.current_stock -= data.quantity
    db.commit()
    db.refresh(product)

    return {
        "message": "Stock removed successfully",
        "current_stock": product.current_stock
    }


# ----------------------------
# LOW STOCK ALERTS
# ----------------------------
@router.get("/alerts/low-stock", response_model=list[ProductOut])
def low_stock_alerts(db: Session = Depends(get_db)):
    products = db.query(Product).filter(
        Product.current_stock <= Product.min_stock
    ).all()

    return products
