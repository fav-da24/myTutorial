# Three Boolean operators - and, or and not

# Binary Boolean Operators - and and or (always take 2 Boolean values, or expressions)
## The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False
print(True and True)        # returns True
print(True and False)       # returns False

## the or operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False.
print(False or True)        # returns True
print(False or False)       # returns False

# Unary Operator - not (operates on only one Boolean value, or expression)
print( not True)            # returns False
print(not not not not True) # returns True

# Mixing Boolean and Comparison Operators
print((4 < 5) and (5 < 6))      # returns True
print((4 < 5) and (9 < 6))      # returns False
print((1 == 2) or (2 == 2))     # returns True
print((2 + 2 == 4) and not (2 + 2 == 5) and (2 * 2 == 2 + 2))   # returns True
