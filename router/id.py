from fastapi import Depends, APIRouter
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_id

router= APIRouter(
    prefix = '/details',
    tags = ['Details']
)

#get details by ID
@router.get('/{id}')
def get_transaction_detail(id: int, db: Session = Depends(get_db)):
    return db_id.get_details_by_id(db,id)