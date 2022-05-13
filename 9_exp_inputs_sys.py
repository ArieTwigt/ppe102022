from handy_functions.calculation_functions import calc_content
import sys

my_length = sys.argv[1]
my_width = sys.argv[2]
my_height = sys.argv[3]

content = calc_content(my_length, my_width, my_height, auto_convert=True)

print(content)