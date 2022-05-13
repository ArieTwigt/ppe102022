#%%
import json

#%%
my_config = {}
my_config['brands'] = ['OPEL', 'PEUGEOT', 'TESLA']

#%% convert the dictionary to a string, that looks like a json object
my_config_str = json.dumps(my_config)

# %%
with open("car_config.json", "w") as file:
    file.write(my_config_str)
# %%
