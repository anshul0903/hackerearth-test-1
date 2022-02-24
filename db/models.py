from sqlalchemy.sql.sqltypes import String, Integer
from sqlalchemy import Column
from db.database import Base
# from sqlalchemy.orm import relationship

class AccountModel(Base):
    __tablename__='Account'
    id = Column(Integer, primary_key=True, index=True, nullable= False)
    account_no = Column(Integer)
    date = Column(String, nullable= False)
    transaction_details = Column(String, nullable= False)
    value_date = Column(String, nullable= False)
    withdrawl_amt = Column(String, nullable= False)
    deposit_amt = Column(String, nullable= False)
    balance_amt = Column(String, nullable= False)

class Modeltest(Base):  #to test to_sql() of pandas, IT WORKS
    __tablename__='Accounts'
    id = Column(String, primary_key=True, index=True, nullable= False)
    account_no = Column(String)
    date = Column(String, nullable= False)
    transaction_details = Column(String, nullable= False)
    value_date = Column(String, nullable= False)
    withdrawl_amt = Column(String, nullable= False)
    deposit_amt = Column(String, nullable= False)
    balance_amt = Column(String, nullable= False)