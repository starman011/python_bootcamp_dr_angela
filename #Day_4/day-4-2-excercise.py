# program to pick random name out of Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random
names_string = len(names)
random_choice = random.randint(0, names_string - 1)
names_string = names[random_choice]

print(f"{names_string} is going to buy  the meal today")

# or we could have used random.choice()