from fastapi import FastAPI
from db import models
from db.database import engine
from router import transactions, balance, accounts, id
from fastapi.staticfiles import StaticFiles

application = FastAPI()

application.include_router(accounts.router)   #created this to test my api
application.include_router(transactions.router) #to display transactions by date
application.include_router(balance.router) #to display balance amount 
application.include_router(id.router) #to display by id


models.Base.metadata.create_all(engine)

application.mount('/files', StaticFiles(directory='files'), name='files')