print("a)")
numbers = range(5)
print(numbers)

print("b)")
numbers = range(5)
for number in numbers:
    print(number)

print("c)")
numbers = range(5, 10)  # if there are 2 value, first value will be considered as starting value and the second value will be considered as ending value, but excluding the ending number
for number in numbers:
    print(number)

print("d)")
numbers = range(5, 10, 2)  # third value will be used as a step
for number in numbers:
    print(number)

print("e)")
for number in range(5):  # for a cleaner code, we can call the range function in here and not as separate variable
    print(number)