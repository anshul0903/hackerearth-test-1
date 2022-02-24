import requests
import json

account = []
new_account = []

response = requests.get("https://s3-ap-southeast-1.amazonaws.com/he-public-data/bankAccountdde24ad.json")
result = response.json()

# def name_change():  #This didnt work
#     new_name = {
#         "Account No": "account_no",
#         "Date": "date",
#         "Transaction Details": "transaction_details",
#         "Value Date": "value_date",
#         "Withdrawal AMT": "withdrawl_amt",
#         "Deposit AMT": "deposit_amt",
#         "Balance AMT": "balance_amt"
#     }

#     for row in account:
#         for key, value in new_name.items():
#             for old_name in row:
#                 if key == old_name:
#                     row[value]=row.pop(old_name)

#     return account


def name_change_two(): #this worked "IMPORTANT"
    global result
    new_names= ["account_no", "date", "transaction_details", "value_date", "withdrawl_amt", "deposit_amt", "balance_amt"]
    global new_account
    for rows in result:
        new_account.append(dict(zip(new_names,list(rows.values()))))
    return new_account
    