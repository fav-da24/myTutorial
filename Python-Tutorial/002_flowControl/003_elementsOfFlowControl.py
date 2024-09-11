# Flow control statements often start with a part called the condition and are always followed by a block of code called the clause

# Conditions
# - The Boolean expressions you’ve seen so far could all be considered conditions, which are the same thing as expressions;
# - condition is just a more specific name in the context of flow control statements
# - Conditions always evaluate down to a Boolean value, True or False
# - almost every flow control statement uses a condition

# Blocks of Code
# - Lines of Python code can be grouped together in blocks
# - You can tell when a block begins and ends from the indentation of the lines of code
# - 3 rules for blocks:
    # - Blocks begin when the indentation increases.
    # - Blocks can contain other blocks.
    # - Blocks end when the indentation decreases to zero or to a containing block’s indentation.

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')            # 1 - The first block of code starts at the line print('Hello, Mary') and contains all the lines after it
    if password == 'swordfish':
        print('Access granted.')    # 2 - Inside this block is another block, which has only a single line in it: print('Access Granted.')
    else:
        print('Wrong password.')    # 3 - The third block is also one line long: print('Wrong password.').
