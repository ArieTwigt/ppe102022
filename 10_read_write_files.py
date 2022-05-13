#%%
file = open("my_text.txt", "a")
file.write("Dit is nieuwe tekst")

file.close()

# %%
with open("my_second_text.txt", "a") as file:
    file.write("Dit is mijn tekst\n")

print("De rest van code")
# %%


## Inlezen van bestanden
#%%
with open("my_second_text.txt", "r") as file:
    content = file.read()

#%%
with open("my_second_text.txt", "r") as file:
    content_list = file.readlines()


#%%
with open("my_second_text.txt", "r") as file:
    content_list = file.readlines()[:5]

# %%


