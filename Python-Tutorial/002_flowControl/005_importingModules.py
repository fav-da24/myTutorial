# Importing MOdules
# - python comes with a set of modules called the standard library
# - Each module is a Python program that contains a related group of functions that can be embedded in your programs
# - Before you can use the functions in a module, you must import the module with an import statemen
# - import statement consists of:
    # - the import keyword
    # - the name of the module
    # - optionally, more module names, as long as they are separated by commas

import random
for i in range(5):
    print(random.randint(1, 10))

# - Here’s an example of an import statement that imports four different modules:

import random, sys, os, math


# from Import Statements
# - is an alternative form of the import statement
# - example: `from random import *`
# - with this, there is no need the `random.` prefix
# - However, using the full name makes for more readable code, so it is better to use the import random form of the statement


# Ending a program early with the `sys.exit()` function
# - Programs always terminate if the program execution reaches the bottom of the instructions.
# - However, you can cause the program to terminate, or exit, before the last instruction by calling the `sys.exit()` function.
# - Since this function is in the `sys` module, you have to import `sys` before your program can use it.

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')