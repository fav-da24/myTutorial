# we use logical operators to build complex rules and conditions

price = 25
print(price > 10 and price < 30)  # logical operator is 'and'. the result we get will be True if both expressions are True.

""" we also have:

price = 5
print(price > 10 or price < 30)  # if at least one of these boolean expressions return True, then the result of this entire expression will be True

price = 5
print(not price > 10)  # basically inverses any values that you give. instead of getting False, we get True """