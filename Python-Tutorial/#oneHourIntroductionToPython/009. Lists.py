# we use lists whenever we want to represent a list of objects, like a list of nmbers or list of names

"""names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
print(names[0])  # to get the first element in the lists
print(names[-1])  # to get the last element in the lists
print(names[-2])  # to get the second last element in the lists"""

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names)
print(names[0:3])  # this will create a new lists. the original one still stay.