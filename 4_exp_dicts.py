#%%
person_dict = {}

#%%
person_dict['name'] = 'arie'
# %%
person_dict['name']
# %%
person_dict['age']
# %%
person_dict.keys()
# %%
person_dict.values()
# %%
person_dict['age'] = 45
# %% 
person_dict['hobbies'] = ['reading', 'cycling', 'gaming'] # list

# %%
person_dict['hobbies'][1]
# %%
person_dict['laptop'] = {'name': 'Dell', 
                         'ram': 500} # dictionary
# %%
person_dict                                                           
# %%
person_dict.keys()
# %%
person_dict['laptop']
# %%


## familieboom

#%%



#%%
person_1 = {"name": "John", "age": 40} 
person_2 = {"name": "Mary", "age": 43}
person_3 = {"name": "Jim", "age": 14, "hobbies": ['gaming', 'football']}
person_4 = {"name": "Rose", "age": 20}


#%%
family_dict = {}
family_dict['name'] = 'Jones'
family_dict['members'] = [person_1, person_2, person_3, person_4]

# %%
family_dict['members'][2]['hobbies'][0]

# %%
