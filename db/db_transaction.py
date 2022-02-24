from db.schema import DbAccount
from db.models import AccountModel
from sqlalchemy.orm.session import Session
from db.config import new_account, result

#get transactions by date
def get_transaction_detail(db: Session, date_in: str):
    date = date_in.split("-")
    global new_account
    ans = []
    for i in range(1,len(date)):
        if date[i] == "01":
            date[i] = "Jan"
        elif date[i] == "02":
            date[i] = "Feb"
        elif date[i] == "03":
            date[i] = "Mar"
        elif date[i] == "04":
            date[i] = "Apr"
        elif date[i] == "05":
            date[i] = "May"
        elif date[i] == "06":
            date[i] = "Jun"
        elif date[i] == "07":
            date[i] = "Jul"
        elif date[i] == "08":
            date[i] = "Aug"
        elif date[i] == "09":
            date[i] = "Sep"
        elif date[i] == "10":
            date[i] = "Oct"
        elif date[i] == "11":
            date[i] = "Nov"
        elif date[i] == "12":
            date[i] = "Dec"
    date = ' '.join(date)  #converts date[type list] into strings
    # return db.query(AccountModel).filter(AccountModel.date == date).all()  #if inserted into db use this
    for row in result:
        if row['Date']  == date:
            ans.append(row)
    return ans