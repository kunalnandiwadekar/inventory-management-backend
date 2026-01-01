from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierOut
from app.deps import get_db

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.post("", response_model=SupplierOut)
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    db_supplier = Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier   # ✅ RETURN ORM OBJECT


@router.get("", response_model=list[SupplierOut])
def get_suppliers(db: Session = Depends(get_db)):
    return db.query(Supplier).all()   # ✅ RETURN ORM LIST


@router.get("/{supplier_id}", response_model=SupplierOut)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    return supplier


@router.put("/{supplier_id}", response_model=SupplierOut)
def update_supplier(
    supplier_id: int,
    updated: SupplierCreate,
    db: Session = Depends(get_db)
):
    supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    for key, value in updated.dict().items():
        setattr(supplier, key, value)

    db.commit()
    db.refresh(supplier)
    return supplier


@router.delete("/{supplier_id}")
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    db.delete(supplier)
    db.commit()
    return {"message": "Supplier deleted successfully"}
