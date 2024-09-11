""" # my try
weight = input("Weight: ")
uom = input("(K)g or (L)bs: ")
if uom == "l":
    print("Weight in Lbs: " + str(int(weight) * 2.20462))
elif uom == "L":
    print("Weight in Lbs: " + str(int(weight) * 2.20462))
elif uom == "k":
    print("Weight in Kgs: " + str(weight))
elif uom == "K":
    print("Weight in Kgs: " + str(weight))
else:
    print("Please insert 'k', 'K', 'l', or 'L' only")
    print("Try again!")"""

# answer
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "L":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
elif unit.upper() == "K":
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))