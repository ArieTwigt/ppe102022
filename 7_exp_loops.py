#%%
name_list = ['arie', 'james', 'henk', 'karin']

for name in name_list:
    print(name)

# %%
for idx, name in enumerate(name_list):
    print(f"De naam {name} staat op positie {idx + 1}")

# %%
import datetime

current_time = datetime.datetime.now()
current_time_10secs = current_time + datetime.timedelta(seconds=10)

# %% Caution, this is still an infinite loop
#while current_time < current_time_10secs:
    
    #print("We zijn bezig")

# %%
