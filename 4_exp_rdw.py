#%%
import requests
import pandas as pd


# %%
response = requests.get("https://opendata.rdw.nl/resource/m9d7-ebf2.json")

# %%
car_list = response.json()

# %%
car_list[0]
# %%
car_list[0]['kenteken']
# %%

# %%
cars_df = pd.DataFrame(car_list)


#%%
cars_df.query("merk == 'FORD'")

# %%
cars_df.to_csv("cars_exported.csv", index=False, sep=";")
# %%
