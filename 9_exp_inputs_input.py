from handy_functions.calculation_functions import calc_content

my_length = input("What is the length?\n")
my_width = input("What is the width?\n")
my_height = input("What is the height?\n")

my_content = calc_content(my_length, my_width, my_height, auto_convert=True)

print(my_content)
print("First line")

print("Second line")