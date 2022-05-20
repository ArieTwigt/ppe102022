## Assignments

# Assignment 1
## Define a function that returns the contents (e.g. in m3) of a box. It takes 3 parameters: (1) Length, (2) width and (3) heigth

#%% Defining the function
def calc_content(length, width, height):
    '''
    A function that calculates the content

    arguments:
    - length (int/float), (required)
    - width (int/float), (required)
    - height (int/float), (required)

    '''

    content = length * width * height
    return content


#%% using the function
result = calc_content(10, 4, 5)
print(result)

# Assignment 2
## Define a function that accepts a lists, capitalizes every name in the list, and retuns this capitalized list. You can use: ['Jim', 'John', 'Marc', 'Danny', 'Peter']


#%% define the function
def capitalize_list(names_list: list, auto_convert=False) -> list:

    # validate the input as a list
    if type(names_list) != list:
        if auto_convert:
            names_list = [names_list]
        else:
            raise TypeError("The input should be a list")


    new_list = []
    
    for name in names_list:
        name_capitalized = name.capitalize()
        new_list.append(name_capitalized)
    
    return new_list



# %% define the names list
my_names = ['jim', 'john', 'marc', 'danny', 'peter']

#%%
capitalize_list(my_names)

#%% apply the function
capitalize_list("jan", auto_convert=True)


# %%

naam = "Arie"


for name in naam:
    print(name)
# %%
