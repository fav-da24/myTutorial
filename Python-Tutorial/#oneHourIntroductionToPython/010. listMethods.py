numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # to add new element
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)  # insert numbers in between elements. 0 represent index/where to insert. -1 represents the object we insert.
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)  # to remove element
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.clear()  # to clear all of the element
print(numbers)

numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # to check whether 1 is in the numbers lists. it return boolean value

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # return the number of elements in a lists