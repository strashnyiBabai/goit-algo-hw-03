import datetime


'''Function "get_gays_from_today" returns the difference (in days) between today's date and
given date in parameters by using their toordinal form. 
Date should be in YYYY-MM-DD or YYYY.MM.DD format otherwise the function will cath error.'''

def get_days_from_today(date: str):

    now = datetime.datetime.now()
    today_toordinal = now.toordinal()

    # try to procces given date by turning one into comprehensible form
    try:
        for punctuation in date:
                if punctuation == "-":
                        date = date.replace("-", ".")

        # turn 'date' into datetime object
        datetime_date = datetime.datetime.strptime(date, "%Y.%m.%d")
        datetime_date = datetime_date.toordinal()


        return today_toordinal - datetime_date
    

    except (ValueError):
        return f"Date '{date}' has wrong format. Use date in YYYY-MM-DD or YYYY.MM.DD format"

    
print(get_days_from_today("2024-03-08"))