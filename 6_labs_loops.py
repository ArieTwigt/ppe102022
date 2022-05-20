## Assignments

#%% 1a
vowels = ['a', 'e', 'o', 'u', 'i']
names_list  =['Jim', 'John', 'Marc', 'Danny', 'Peter']


# create a new empty list that will be filled by the loop
new_names_list = []

# iterate over the names list and remove the vowels in each name
for name in names_list:
    print(name)
    for letter in name:
        if letter.lower() in vowels:
            name = name.replace(letter, "") # replace the vowel for an empty string (removing the letter)
    
    print(name)
    new_names_list.append(name)


print(new_names_list)


# %% 2a.
import datetime

# (optioneel, als je de taal/locale gegevens wilt wijzigen)
import locale 

locale.setlocale(locale.LC_ALL, "nl_NL")

current_date = datetime.date.today()

day_range = range(1,11) # starts with 1, ends by 10

for num_days in day_range:
    new_date = current_date + datetime.timedelta(days = num_days)
    print(new_date.strftime("%A")) # strftime.org --> voor verschillende data formaten


#%% 2b. 
import locale 

locale.setlocale(locale.LC_ALL, "nl_NL")


# %%
