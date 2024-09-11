# When you call the print() or len() function, you pass them values, called arguments, by typing them between the parentheses.
# You can also define your own functions that accept arguments

def hello(name):                # 1 - The definition of the hello() function in this program has a parameter called name
                                #   - Parameters are variables that contain arguments
                                #   - When a function is called with arguments, the arguments are stored in the parameters

    print('Hello, ' + name)     # 3 - The program execution enters the function, and the parameter name is automatically set to 'Alice', which is what gets printed by the print() statement

hello('Alice')                  # 2 - The first time the hello() function is called, it is passed the argument 'Alice'
hello('Bob')
