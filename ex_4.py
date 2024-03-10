import datetime

# test list
users = ({"name" : "Anrdrij", "birthday" : "2008-03-06"}, {"name" : "Lerun'ka", "birthday" : "1999-03-12"}, {"name" : "Natalia", "birthday" : "1978-03-10"}, {"name" : "Bababoy", "birthday" : "1900.03.16"})


"""returns people to congradulate if their birthday is during next 7 day.
As a parameters requires list with dictionaries e.g. ({"name" : "Anrdrij", "birthday" : "2008-03-06"}, {"name" : "Lerun'ka", "birthday" : "1999-03-12"}).
If birthday is on weekend than get_upcoming_birthdays shifts the congradulation day to next Monday."""

def get_upcoming_birthdays(users):
    today = datetime.datetime.today().date()
    birthday_is_in_this_week = None
    congratulation_date = None
    weekdays = range(0, 5)
    to_cogradulate = []

#     parse all given users and their birthdays
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # check if input date punctuations are acceptable, otherwise change it to acceptable ones
        for punctuation in birthday:
                if punctuation == "-":
                        birthday = birthday.replace("-", ".")

        # turn 'birthday' into datetime object
        birthday_to_datetime_obj = datetime.datetime.strptime(birthday, "%Y.%m.%d").date()
        birthday_this_year = datetime.datetime(year=today.year, month=birthday_to_datetime_obj.month, day=birthday_to_datetime_obj.day).date()
        birthday_is_in_this_week = (today + datetime.timedelta(days=7)) > birthday_this_year >= today

        """check for the next seven days if there are any birthdays. 
        If yes check if they are on weekdays and scedule the congradulation.
        If birthday on weekend scedule congradulations for next Monday"""
        if birthday_is_in_this_week:
                congratulation_date = birthday_this_year
                if birthday_this_year.weekday in weekdays:
                       to_cogradulate.append({f"{name}" : f"{congratulation_date}"},)
                else:
                        while congratulation_date.weekday() not in weekdays:
                                congratulation_date += datetime.timedelta(days=1)

                        to_cogradulate.append({f"{name}" : f"{congratulation_date}"},)
    
    
    return to_cogradulate
