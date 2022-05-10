#%%
name = "arie"


#%%
length = 1.93

#%% Everything is an object
# an object has 'methods' and 'attributes'
name.upper()
# %%


# %% a function is global
len(name)
# %%
4 + 4
# %%
name + name
# %%
'4' + "4"

# %%
names_1 = ['arie', 'jaap']
names_2 = ['dirk', 'jan']
names_1 + names_2
# %%
length + length
# %%
length + name
# %%
str(length) + name


# %%
list(name)
# %%
# %%
name = "arie"
last_name = "twigt"

# %%
name + " " + last_name
# %% formatting (available since Python 2)
"{} {}".format(name, last_name)

# %%
"Hoe gaat het met jou {}?".format(name)

#%% f-strings (available since Python 3)
f"{name} {last_name}"


# %%
print(f"My name is {name.capitalize()}, and my last \nname is {last_name.capitalize()}, so {name} is the name")
print(name)

#%%
# %%
f"My name is {name.capitalize()}, and my last \nname is {last_name.capitalize()}, so {name} is the name"
# %%
name.capitalize() # call, callable
# %%
name.capitalize # describe
# %%
