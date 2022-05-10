#%%
import datetime
import sys

# %%
birthday_month = int(input("What is your birthday month?\n")) # int(sys.argv[1])

# check the month value
if birthday_month not in range(1, 13):
    raise ValueError("The month must be between 1 and 12")
    sys.exit()

birthday_day = int(input("What is your birthday day?\n")) #int(sys.argv[2])

# check the day value
if birthday_day not in range(1, 32):
    raise ValueError("The day wrong")
    sys.exit()

# get the current date
current_date = datetime.date.today()

# set the birthday date for the current year
current_year = datetime.date.today().year
curren_year_birthday = datetime.date(current_year, birthday_month, birthday_day)

# check if my birthday already passed this year
birthday_passed = current_date > curren_year_birthday

if birthday_passed:
    next_year = current_year + 1
    next_birthday = datetime.date(next_year, birthday_month, birthday_day)
    days_until_birthday = (next_birthday - current_date).days
    print(f"Your next birthday is in {days_until_birthday} days")
else:
    next_birthday = datetime.date(current_year, birthday_month ,birthday_day)
    days_until_birthday = (next_birthday - current_date).days
    print(f"Your next birthday is in {days_until_birthday} days")