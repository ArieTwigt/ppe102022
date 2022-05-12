## Assignments

#%% 1a.
name = "Arie"

if "A" in name:
    print("Your name starts with an A!")
else:
    print("Your name does not start with an A :(")

# %% 1b

name = "Arie"

if "a" in name.lower():
    print("Your name starts with an A!")
else:
    print("Your name does not start with an A :(")


#%% 2a.
name = "Arie"

vowels = ['a', 'e', 'o', 'u', 'i']

if name[0].lower() in vowels:
    name = name.replace(name[0], "B")
    print(name)
else:
    name = name.replace(name[0], "E")
    print(name)



# %% 2b. Meer generiek
import random
import string

name = "Arie"

vowels = ['a','e', 'o', 'u', 'i']
letters_list = list(string.ascii_lowercase)

non_vowels = [letter for letter in letters_list if letter not in vowels]

if name[0].lower() in vowels:
    print("Your name begins with a vowel")
    random_letter = random.choice(non_vowels)
    random_letter_upper = random_letter.upper()
    name = name.replace(name[0], random_letter_upper)
    print(name)
else:
    print("Your name begins with a vowel")
    random_letter = random.choice(vowels)
    random_letter_upper = random_letter.upper()
    name = name.replace(name[0], random_letter_upper)
    print(name)
# %%
