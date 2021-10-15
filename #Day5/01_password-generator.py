#Password Generator Project'

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
password = ""
for letter in range(1, nr_letters+1):
  a = random.choice(letters)
  password += a
# print(password)
for symbol in range(1, nr_symbols+1):
  b = random.choice(symbols)
  password += b
# print(password)
for number in range(1, nr_numbers+1):
  c = random.choice(numbers)
  password += c
# print(password)

print(f"Here is your password: {password}")

#Hard Level - Order of characters randomised:
password_list = []
for letter in range(1, nr_letters+1):
  a = random.choice(letters)
  password_list += a
# print(password)
for symbol in range(1, nr_symbols+1):
  b = random.choice(symbols)
  password_list += b
# print(password)
for number in range(1, nr_numbers+1):
  c = random.choice(numbers)
  password_list += c
# print(password)
random.shuffle(password_list)

# print(f"Here is your password: {password_list}")
password_list1 = ""
for char in password_list:
  password_list1 += char
print(f"Your password is : {password_list1}")