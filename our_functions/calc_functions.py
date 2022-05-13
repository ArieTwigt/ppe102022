import math


def calc_circle(diameter, rouding=False, round_value=1):
    '''
    This function calculates the surface of a circle

    parameters:
    - diameter (int/float), required
    - rounding (int), optional
    '''

    radius = diameter / 2
    surface = math.pow(radius, 2) * math.pi

    if rouding:
        surface = round(surface, round_value)

    return surface


def calc_pythagoras(A, B):
    C_sqrd = math.pow(A, 2) + math.pow(B, 2)
    C = math.sqrt(C_sqrd)

    return C
