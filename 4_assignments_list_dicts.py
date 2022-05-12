## Assignments

#%% 1a. 
person = {}
person['name'] = "Clark"
person['age'] =  40
person['hobbies'] = ['football', 'tennis', 'mountainbike']


#%% 1b.
person = {'name': 'Clark', 
          'age': 40, 
          'hobbies': ['football', 'tennis', 'mountainbike']}


#%% 2. 
person_2 = {"name": "Mary", "age": 43}
person_3 = {"name": "Jim", "age": 14, "hobbies": ['gaming', 'football']}
person_4 = {"name": "Rose", "age": 20}

#%%
family_dict = {}
family_dict['name'] = "Kent"
family_dict['members'] = [person, person_2, person_3, person_4]


# %%
family_dict

#%% BONUS
# Append the following person to the members of family dict
person_5 = {'name': 'peter', 'age': 0}

#%%
family_dict['members'].append(object)
# %%
