from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductOut
from app.deps import get_db
from app.schemas.stock import StockUpdate

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.post("/{product_id}/stock-in")
def stock_in(product_id: int, data: StockUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.current_stock += data.quantity
    db.commit()
    db.refresh(product)

    return {
        "message": "Stock added successfully",
        "current_stock": product.current_stock
    }

@router.post("/{product_id}/stock-out")
def stock_out(product_id: int, data: StockUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
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

@router.get("/alerts/low-stock")
def low_stock_alerts(db: Session = Depends(get_db)):
    products = db.query(Product).filter(
        Product.current_stock <= Product.min_stock
    ).all()

    return {
        "count": len(products),
        "products": products
    }


@router.get("/dashboard/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    total_products = db.query(Product).count()
    total_stock = db.query(Product).with_entities(
        Product.current_stock
    ).all()

    stock_sum = sum(item[0] for item in total_stock)

    low_stock_count = db.query(Product).filter(
        Product.current_stock <= Product.min_stock
    ).count()

    return {
        "total_products": total_products,
        "total_stock_units": stock_sum,
        "low_stock_products": low_stock_count
    }




@router.get("/", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, updated: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
