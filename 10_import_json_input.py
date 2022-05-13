#%%
import json
import requests
import pandas as pd
import os
import datetime

#%% check if the export folders already exists
current_files_folders = os.listdir()

if "export" not in current_files_folders:
    print("creating export folder")
    os.mkdir("export")

#%%
with open("car_config.json", "r") as file:
    config_str = file.read()

#%% convert the string to a dict
config = json.loads(config_str)

#%%
selected_brands = config['brands']

# %%
for brand in selected_brands:
    print(f"Importing {brand}")
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"

    response = requests.get(endpoint)
    car_list = response.json()
    print(f"Succesfully imported {brand}")

    # check if the folder of this brand already exists
    current_files_folders_brand = os.listdir("export")

    if brand not in current_files_folders_brand:
        print(f"Folder of {brand} does not exists yet")
        os.mkdir(f"export/{brand}")
        print(f"Created folder for {brand}")

    # export the car to a csv
    df = pd.DataFrame(car_list)


    # create a datetime string
    datetime_str = str(datetime.datetime.now()).replace(":", "").replace("-", "").replace(" ", "").replace(".", "")

    # compose the file name
    file_name = f"export/{brand}/{brand}_{datetime_str}.csv"
    
    df.to_csv(file_name, index=False, sep=";", mode='a', header=False)
    print(f"Succesfully exported {brand}")

