# Assignments

#%% Assignment 1
first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name
# %% 1a. 
full_name = first_name + " " + last_name + " " + "Jr."
print(full_name)

# %% 1b. 
full_name = "{} {} Jr.".format(first_name, last_name)
print(full_name)

# %% 1c. 
full_name = f"{first_name} {last_name} Jr."
print(full_name)

# %% Assignment 2.

#%% a. 
full_name_abbrv = full_name.replace("Erling", "E.")
print(full_name_abbrv)


# %% b. 
full_name_split = full_name.split(" ") # split the string into seperate values of a list
first_name = full_name_split[0] # take the first value of the list
first_letter = first_name[0] + "." # assign the first character of the first value
full_name_new = f"{first_letter} {last_name} Jr." # compose the full name
print(full_name_new)

# %% Assignment 3
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2


#%% a. 
print(combined_flower_list)
combined_flower_list[1] = 'daisy'
print(combined_flower_list)


# %% b.
print(combined_flower_list)
idx_tulip = combined_flower_list.index("tulip")
combined_flower_list[idx_tulip] = "daisy"

# %%
