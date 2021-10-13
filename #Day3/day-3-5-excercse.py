#program to make a love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

a = name1 + name2
lowercase = a.lower()
t = a.count("t")
print(f"T occurs{t} times")
r = a.count("r")
print(f"R occurs{r} times")
u = a.count("u")
print(f"U occurs{u} times")
E = a.count("e")
print(f"E occurs{E} times")
z = t+r+u+E
print("Total",z)

L = a.count("l")
print(f"L occurs{L} times")
O = a.count("o")
print(f"O occurs{O} times")
V = a.count("v")
print(f"V occurs{V} times")
E = a.count("e")
print(f"L occurs{E} times")
y = L+O+V+E
print("Total",y)

print("Love Score = ",str(z)+str(y))

score = int(str(z)+str(y))

if score < 10 or score >90 :
  print(f"Your score is {score}, you  go together like coke and mentos.")
elif score <=50 or score>=40:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
