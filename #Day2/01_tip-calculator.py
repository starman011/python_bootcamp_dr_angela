#project to split bills and find the tip also
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

per_tip =int(input("What percentage tip would you like to give? 10, 12, or 15?"))

a = (bill*per_tip/100)+bill
a = round(a,2)
person = int(input("How many people to split the bill?"))

split = int(a)/int(person)
k = round(split,2)
k = "{:.2f}".format(split)
print("Each person should pay: $",k)