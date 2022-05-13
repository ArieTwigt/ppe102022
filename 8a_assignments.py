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