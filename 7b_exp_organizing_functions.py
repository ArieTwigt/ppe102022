from our_functions.calc_functions import calc_circle, calc_pythagoras
from our_functions.replace_functions import replace_letter

my_diameter = int(input("What is the diameter?\n"))

my_circle = calc_circle(my_diameter, rouding=True, round_value=4)

print(my_circle)


print("Now it is time for Pythagoras")

my_A = int(input("What is A? \n"))
my_B = int(input("What is B? \n"))

my_C = calc_pythagoras(my_A, my_B)
print(my_C)

print("Now let's replace a name")
my_name = input("What is the name?\n")

my_name_converted = replace_letter(my_name)
print(my_name_converted)