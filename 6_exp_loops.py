#%%
names_list = ['arie', 'jim', 'hans', 'jaap', 'erik']

#%%
for i in names_list:
    print(i)

# %%
for name in names_list:
    print(name)

# %%
for name in names_list:
    name_upper = name.upper()
    print(name_upper)

# %%
non_vowel_names = []
vowel_names = []

vowels_list = ['a', 'e', 'o', 'u', 'i']

for name in names_list:
    if name[0].lower() in vowels_list:
        name_capitalized = name.capitalize()
        vowel_names.append(name_capitalized)
    else:
        name_capitalized = name.capitalize()
        non_vowel_names.append(name_capitalized)

# %%
non_vowel_names
# %%
vowel_names
# %%
