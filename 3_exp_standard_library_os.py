#%%
import os
# %%
os.getcwd()
# %%
os.mkdir("my_folder")
# %%
with open("my_folder/my_file.txt", "w") as file:
    file.write("Hello") 
# %%
os.listdir()
# %%
os.listdir("my_folder")
# %%
available_files = os.listdir("my_folder")

#%%
file_to_remove = "my_file.txt"


#%%
if file_to_remove in available_files:
    print("Removing file")
    os.remove(f"my_folder/{file_to_remove}")
else:
    print("File not found, proceeding")

# %%
os.rmdir("my_folder")

# %%
