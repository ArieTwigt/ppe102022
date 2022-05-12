#%%
def replace_first_letter(name):
    new_name = name.replace(name[0], "X")
    return new_name

#%%
replace_first_letter("Arie")

# %%
import math


def calc_pythagoras(A, B, rounding=False, rounding_value=1):
    '''
    This function applies the Pythagoras theorem

    parameters:
    - A (required) 
    - B (required)
    - rounding (optional)
    - rounding_value (optional)

    '''


    C_sqrd = math.pow(A, 2) + math.pow(B, 2)
    C = math.sqrt(C_sqrd)

    if rounding:
        C = round(C, rounding_value)

    return C

#%%
calc_pythagoras(4, 4, rounding=True, rounding_value=5)

# %%
