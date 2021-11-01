################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength)#here the previously indented line that's defines ,still gives error

#Global Scope
player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()

#There is no Block scope 
game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]
  print(new_enemy)

#Modifying Global Scope
enemies = 1
def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")
#this is a technique but then its not advisable
increase_enemies()
print(f"enemies outside function: {enemies}")

#Instead use return function to call in
enemies = 1
def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1
#this technique is more easy and uses without modifying a global variable
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constant
PI = 3.14159
def calc():
  PI#this is to remind that this upper case variable should not be modified
