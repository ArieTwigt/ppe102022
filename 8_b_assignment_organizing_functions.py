#%% import the required modules
from handy_functions.calculation_functions import calc_content
from handy_functions.name_functions import capitalize_list

#%%
result = calc_content(10, 50, 3)
print(result)

#%%
my_names = ['arie', 'jan', 'dirk']
my_new_names = capitalize_list(my_names)
print(my_new_names)
# %%
