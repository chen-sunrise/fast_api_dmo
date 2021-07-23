from typing import Optional
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.applications.config.database import Base, engine, SessionLocal
from src.applications.dao.account_entity import AccountEntity

router = APIRouter()
Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/items/")
async def read_items(q: Optional[str] = None, db: Session = Depends(get_db)):
    res = AccountEntity(db).get_accounts()
    # results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    # if q:
    #     results.update({"q": q})
    return res.to_json()


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}