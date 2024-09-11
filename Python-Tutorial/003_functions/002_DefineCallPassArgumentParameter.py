def sayHello(name):             # 1 - the def statement defines the sayHello() function
    print('Hello, ' + name)
sayHello('Al')                  # 2 - the sayHello('Al') line calls the now-created function, sending the execution to the top of the function's code
                                #   - this function call is also known as passing the string value 'Al' to the function
                                # 3 - a value being passed to a function in a function is an argument
                                #   - the argument 'Al' is assigned to a local variable named `name`
                                # 4 - variables that have arguments assigned to them are parameters