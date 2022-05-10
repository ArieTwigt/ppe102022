## Assignments

#%% Assignment
import datetime


#%% a.
next_birthday = datetime.date(2023, 4, 11)
date_today = datetime.date.today()
date_difference = next_birthday - date_today
days_difference = date_difference.days
print(days_difference)

f"My birthday is in {days_difference} days"


# %% b. Generiek
# set the month and day for my birthday (never changes)
birthday_month = 4
birthday_day = 11

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

# %% 2. 
import math

diameter = 10
radius = diameter / 2
surface =math.pow(radius, 2) * math.pi
surface_rounded = round(surface, 4)
print(surface_rounded)

# %% 3.
import os

current_files_folders = os.listdir()
print(current_files_folders)

# %% 4.
os.mkdir("our_functions")

# %%
