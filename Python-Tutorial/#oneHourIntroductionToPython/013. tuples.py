# tuples are immutable, we cannot change them once created

""""#to prove that tuples cannot be changed
# this will get an error, 'tuple' object does not support item assignment
numbers = (1, 2, 3)  # square bracket to define lists, parentheses to define tuples
numbers[0] = 10"""

numbers = (1, 2, 3, 3)
numbers.count(3)  # this will return 2
numbers.index()
numbers.__add__()  # the 2 underscores methods called magic methods, advanced topic