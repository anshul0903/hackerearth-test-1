from typing import List
from fastapi import Depends, APIRouter, File, UploadFile
from sqlalchemy.orm.session import Session
from db.schema import DbAccount
from db.database import get_db
import shutil
import json
from db import config
import pandas as pd
from db.config import new_account, result
from db.database import engine

router = APIRouter(
    tags=['Accounts']
)

# @router.get('/data')
# def create_account(request: List, db: Session = Depends(get_db)):
#     return db_data.create_account_two(db,request)
 
# @router.post('/upload')
# async def uploadFile(file: bytes = File(...)):
#     content = file.decode('utf-8')
#     lines = content.split('\n')
#     with open('files/test.txt') as json_file:
#         account = json.load(json_file)
#     return account



@router.post('/UploadFile')
def upload_file(files: UploadFile = File(...)):
    path = f'files/{files.filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(files.file, buffer)  #in requirments.txt add python-multipart, python-jose, aiofiles
 #shutil.copyfileobj creates the file in the path
    with open('files/test.txt') as json_file:
        config.account = json.load(json_file)

    #config.account = json.dumps(config.account)  #to convert dict into strings, as dict keys can not be changed
    return config.account

@router.get('/get')
def upload_json():
    return config.name_change_two()

# @router.post('/insert')  #to test to_sql(), it works
# def insert(db: Session = Depends(get_db)):
#     global new_account
#     df =[
#             {
#                 'id': '1',
#                 'account_no': '409000611074',
#                 'date': '29 Jun 17',
#                 'transaction_details': 'TRF FROM  Indiaforensic SERVICES',
#                 'value_date': '29 Jun 17',
#                 'withdrawl_amt': '',
#                 'deposit_amt': '10,00,000.00',
#                 'balance_amt': '10,00,000.0'
#             },
#             {
#                 'id':'2',
#                 'account_no': '409000611074',
#                 'date': '29 Jun 17',
#                 'transaction_details': 'TRF FROM  Indiaforensic SERVICES',
#                 'value_date': '29 Jun 17',
#                 'withdrawl_amt': '',
#                 'deposit_amt': '10,00,000.00',
#                 'balance_amt': '10,00,000.0'
#             }
#         ]
#     account_df = pd.DataFrame.from_dict(df)
#     account_df.to_sql('Accounts', engine, if_exists='append',index=False) #if db isnt created it will create a new one
#     return account_df
    
@router.put('/add')  #add new data to existing json
def add_data(account_no : int, date: str, transaction_details: str, value_date: str, withdrawl_amt:str,deposit_amt: str, balance_amt:str):
    global result
    data = {     
    "Account No": account_no,
    "Date": date,
    "Transaction Details": transaction_details,
    "Value Date": value_date,
    "Withdrawal AMT": withdrawl_amt,
    "Deposit AMT": deposit_amt,
    "Balance AMT": balance_amt
    }

    result.append(data)
    return data

@router.get('/details')
def get_all():
    return result
    


