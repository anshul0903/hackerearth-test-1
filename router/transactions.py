from fastapi import Depends, APIRouter
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_transaction

router = APIRouter(
    prefix='/transaction',
    tags=['Transaction']
)

#get transactions by date
@router.get('/{date_in}')
def get_transaction_detail(date_in: str, db: Session = Depends(get_db)):
    return db_transaction.get_transaction_detail(db, date_in)
