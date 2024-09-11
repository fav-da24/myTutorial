# if Statements
# - An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True.
# - The clause is skipped if the condition is False.
# - consists of:
    # - The if keyword
    # - A condition (that is, an expression that evaluates to True or False)
    # - A colon
    # - Starting on the next line, an indented block of code (called the if clause)

name = 'Alice'
if name == 'Alice':
    print('Hi, Alice')


# else Statements
# - An if clause can optionally be followed by an else statement.
# - The else clause is executed only when the if statement’s condition is False.
# - An else statement doesn’t have a condition
# - consists of:
    # - The else keyword
    # - A colon
    # - Starting on the next line, an indented block of code (called the else clause)

name = 'Ali'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')


# elif Statements
# - While only one of the if or else clauses will execute, you may have a case where you want one of many possible clauses to execute.
# - The elif statement is an “else if” statement that always follows an if or another elif statement.
# - It provides another condition that is checked only if all of the previous conditions were False.
# - consists of:
    # - The elif keyword
    # - A condition (that is, an expression that evaluates to True or False)
    # - A colon
    # - Starting on the next line, an indented block of code (called the elif clause)

name = 'Alice'
age = 13
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')


# while Loop Statements
# - You can make a block of code execute over and over again using a while statement.
# - The code in a while clause will be executed as long as the while statement’s condition is True.
# - consists of:
    # - The while keyword
    # - A condition (that is, an expression that evaluates to True or False)
    # - A colon
    # - Starting on the next line, an indented block of code (called the while clause)
# - difference between while statement and if statement is:
    # - At the end of an if clause, the program execution continues after the if statement
    # - at the end of a while clause, the program execution jumps back to the start of the while statement
# - The while clause is often called the while loop or just the loop

# code with an if statement:
spam = 0
if spam < 5:
    print('Hello, World')
    spam = spam + 1

# code with a while statement:
spam = 0
while spam < 5:
    print('Hello, World')
    spam = spam + 1

# - In the while loop, the condition is always checked at the start of each iteration (that is, each time the loop is executed).
# - If the condition is True, then the clause is executed, and afterward, the condition is checked again.
# - The first time the condition is found to be False, the while clause is skipped


# Annoying while Loop Statements
name = ''                               # 1 - First, the program sets the name variable to an empty strin
while name != 'your name':              # 2 - This is so that the name != 'your name' condition will evaluate to True and the program execution will enter the while loop’s clause
    print('Please type your name.')
    name = input()                      # 3 - The code inside this clause asks the user to type their name, which is assigned to the name variable
print('Thank you!')                     # 4 - Since this is the last line of the block, the execution moves back to the start of the while loop and reevaluates the condition.
                                        #   - If the value in name is not equal to the string 'your name', then the condition is True, and the execution enters the while clause again.
                                        #   - But once the user types your name, the condition of the while loop will be 'your name' != 'your name', which evaluates to False.
                                        #   - The condition is now False, and instead of the program execution reentering the while loop’s clause, Python skips past it and continues running the rest of the program


# break Statements
# - shortcut to getting the program execution to break out of a while loop's clause
# - simply contains the break keyword

while True:                             # 1 - The first line creates an infinite loop; it is a while loop whose condition is always True.
                                        #   - (The expression True, after all, always evaluates down to the value True.)
                                        #   - After the program execution enters this loop, it will exit the loop only when a break statement is executed.
                                        #   - (An infinite loop that never exits is a common programming bug.)
    print('Please type your name.')
    name = input()                      # 2 - Just like before, this program asks the user to enter your name
    if name == 'your name':             # 3 - Now, however, while the execution is still inside the while loop, an if statement checks whether name is equal to 'your name'
        break                           # 4 - If this condition is True, the break statement is run
print('Thank you!')                     # 5 - and the execution moves out of the loop to print('Thank you!')
                                        #   - Otherwise, the if statement’s clause that contains the break statement is skipped, which puts the execution at the end of the while loop.
                                        #   - At this point, the program execution jumps back to the start of the while statement ➊ to recheck the condition


# continue Statements
# - used inside loops
# - When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition.
# - (This is also what happens when the execution reaches the end of the loop.)

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    print('Access granted.')


# for Loops and the range() Function
# - what if you want to execute a block of code only a certain number of times?
# - You can do this with a for loop statement and the range() function.
# - in code, a for statement looks something like for i in range(5): and includes the following:
    # - The for keyword
    # - A variable name
    # - The in keyword
    # - A call to the range() method with up to three integers passed to it
    # - A colon
    # - Starting on the next line, an indented block of code (called the for clause)

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# - You can use break and continue statements inside for loops as well.
# - The continue statement will continue to the next value of the for loop’s counter, as if the program execution had reached the end of the loop and returned to the start.
# - In fact, you can use continue and break statements only inside while and for loops.
# - If you try to use these statements elsewhere, Python will give you an error.
# - another for loop example:

total = 0
for num in range(101):
    total = total + num
print(total)


# an equivalent while loop
# - You can actually use a while loop to do the same thing as a for loop; for loops are just more concise

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1


# The Starting, Stopping, and Stepping Arguments to range()

for i in range(12, 16):
    print(i)                # print results 12 13 14 15 16

# - range() function can also be called with three arguments.
    # - first two arguments will be the start and stop values
    # - the third will be the step argument

for i in range(0, 10, 2):
    print(i)                # print results 0 2 4 6 8

# - The range() function is flexible in the sequence of numbers it produces for for loops
# - you can even use a negative number for the step argument to make the for loop count down instead of up

for i in range (5, -1, -1):
    print(i)                # results 4 3 2 1 0



