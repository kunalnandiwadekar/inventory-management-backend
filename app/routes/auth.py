from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.auth import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# demo admin credentials
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "admin123"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    #  DEMO ADMIN LOGIN 
    if username == DEMO_USERNAME and password == DEMO_PASSWORD:
        token = create_access_token({"sub": username})
        return {
            "access_token": token,
            "token_type": "bearer"
        }

    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }
