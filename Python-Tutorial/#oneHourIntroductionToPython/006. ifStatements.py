# we use if statements to make decisions in our programs

temperature = 11
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")  # to terminate this block we press enter and then press shift and tab.
elif temperature > 20:  # if the temp greater than 20 and less than or equal to 30
    print("It's a nice day")
elif temperature > 10:  # if the temp greater than 10 and less than or equal to 20
    print("It's a bit cold")
else: # this code will be executed if none of the above conditions are True
    print("It's cold")
print("Done")