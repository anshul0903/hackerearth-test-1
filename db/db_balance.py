from db.config import result

#get balance amount
def get_balance_detail(date_in : str):
    date = date_in.split("-")
    for i in range(len(date)):
        if date[i] == "01":
            date[i] = "Jan"
        if date[i] == "02":
            date[i] = "Feb"
        if date[i] == "03":
            date[i] = "Mar"
        if date[i] == "04":
            date[i] = "Apr"
        if date[i] == "05":
            date[i] = "May"
        if date[i] == "06":
            date[i] = "Jun"
        if date[i] == "07":
            date[i] = "Jul"
        if date[i] == "08":
            date[i] = "Aug"
        if date[i] == "09":
            date[i] = "Sep"
        if date[i] == "10":
            date[i] = "Oct"
        if date[i] == "11":
            date[i] = "Nov"
        if date[i] == "12":
            date[i] = "Dec"
    date = ' '.join(date)
    # account = db.query(AccountModel).filter(AccountModel.date == date).first()
    for row in result:
        if row['Date']  == date:
            return row
