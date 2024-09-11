name = input("What is your name? ") #input function
print("Hello " + name)

birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year) #to subtract string into integer, write int(). birth_year only print string.
print(age)

# int() #convert value to integer
# float() #convert value to floating point number
# bool() #convert value to boolean (True/False)
# str() #convert value to string

""" first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second) #adding float number
print("Sum: " + str(sum)) """

""" first = float(input("First: ")) #another way to adding float number
second = float(input("Second: ")) #another way to adding float number
sum = first + second
print("Sum: " + str(sum)) """

""" course = 'Python for Beginners'
print(course.replace('for','4')) #method replace """

""" course = 'Python for Beginners'
print('Python' in course) #in operator to find Python in course """

