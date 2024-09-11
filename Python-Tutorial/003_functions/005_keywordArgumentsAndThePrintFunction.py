# keyword arguments are identified by the keyword put before them in the function call
# Keyword arguments are often used for optional parameters
# For example, the print() function has the optional parameters end and sep to specify what should be printed at the end of its arguments and between its arguments (separating them), respectively

print('Hello')
print('World')
# this will returns Hello and World on separate lines

# end keyword argument
print('Hello', end='')
print('World')
# this will returns HelloWorld

print('cats', 'dogs', 'mice')
# this will returns cats dogs mice

# sep keyword argument
print('cats', 'dogs', 'mice', sep=',')
# returns cats,dogs,mice

