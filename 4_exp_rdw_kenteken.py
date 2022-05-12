#%%
import requests
import sys


selected_kenteken = input("Selecteerd kenteken\n")
selected_kenteken = selected_kenteken.upper()

#%%
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={selected_kenteken}"

#%%
response = requests.get(endpoint)

# %%
car = response.json()

#%%
if len(car) == 0:
    print(f"No car found for {selected_kenteken}")
    sys.exit()


car = car[0]

#%%
merk = car['merk']
handelsbenaming = car['handelsbenaming']
# %%
print(f"Dit is een {merk} van het type {handelsbenaming}")
# %%
