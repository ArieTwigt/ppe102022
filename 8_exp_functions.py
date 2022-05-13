#%%
def replace_first_letter(name):
    new_name = name.replace(name[0], "X")
    return new_name

#%%
replace_first_letter("Arie")

# %%
import math


def calc_pythagoras(A, B=None, rounding=False, rounding_value=1, export_as_dict=False):
    '''
    This function applies the Pythagoras theorem

    parameters:
    - A (required) 
    - B (required)
    - rounding (optional)
    - rounding_value (optional)

    '''
    

    global C_sqrd
    C_sqrd = math.pow(A, 2) + math.pow(B, 2)

    C = math.sqrt(C_sqrd)

    if rounding:
        C = round(C, rounding_value)

    if export_as_dict:
        return {"A": A,
                "B": B,
                "C": C}
    else:         
        return C, C_sqrd


#%%
result = calc_pythagoras(4)

# %%
