from db.models import AccountModel
from sqlalchemy.orm.session import Session

#get details by ID
def get_details_by_id(db: Session, id : int):
    return db.query(AccountModel).filter(AccountModel.account_no == id).all()