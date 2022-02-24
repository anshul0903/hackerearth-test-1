from pydantic import BaseModel

class DbAccount(BaseModel):
    account_no: int
    date : str
    transaction_details : str
    value_date : str
    withdrawl_amt : str
    deposit_amt : str
    balance_amt : str
