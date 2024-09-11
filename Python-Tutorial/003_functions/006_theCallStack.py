# Python will remember which line of code called the function so that the execution can return there when it encounters a return statement.
# If that original function called other functions, the execution would return to those function calls first, before returning from the original function call.
# abcdCallStack.py

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

