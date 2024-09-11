spam = 40           # ➊
print(spam)

eggs = 2
print(spam + eggs)  # ➋

print(spam + eggs + spam)

spam = spam + 2     # ➌
print(spam)

# A variable is initialized (or created) the first time a value is stored in it ➊.
# After that, you can use it in expressions with other variables and values ➋.
# When a variable is assigned a new value ➌, the old value is forgotten, which is why spam evaluated to 42 instead of 40 at the end of the example.