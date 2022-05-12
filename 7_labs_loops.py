## Assignments

#%% 1a
vowels = ['a', 'e', 'o', 'u', 'i']
names_list  =['Jim', 'John', 'Marc', 'Danny', 'Peter']


# create a new empty list that will be filled by the loop
new_names_list = []

# iterate over the names list and remove the vowels in each name
for name in names_list:
    print(name)
    for letter in name:
        if letter.lower() in vowels:
            name = name.replace(letter, "") # replace the vowel for an empty string (removing the letter)
    
    print(name)
    new_names_list.append(name)


print(new_names_list)


# %%
