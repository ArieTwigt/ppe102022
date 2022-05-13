def calc_content(length, width, height, auto_convert=False):
    '''
    A function that calculates the content

    arguments:
    - length (int/float), (required)
    - width (int/float), (required)
    - height (int/float), (required)

    '''
    
    if auto_convert:
        length = float(length)
        width = float(width)
        height = float(height)


    content = length * width * height

    return content