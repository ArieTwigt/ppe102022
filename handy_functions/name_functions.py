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