from fastapi import Depends, APIRouter
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_balance

router= APIRouter(
    prefix = '/balance',
    tags = ['Balance']
)

#get balance amount
@router.get('/{date_in}')
def get_transaction_detail(date_in: str, db: Session = Depends(get_db)):
    return db_balance.get_balance_detail(db, date_in)