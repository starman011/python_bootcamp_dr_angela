#program to make a rock, paper and scissor game.
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#code for user
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input == 0:
  print(rock)
elif user_input == 1:
  print(paper)
elif user_input == 2:
  print(scissors)

#code for computer
print("Computer chose:")


outcome = [rock, paper, scissors]
len_outcome = int(len(outcome))

random_list =int(random.randint(0, 2))
if random_list == 0:
  print(rock)
elif random_list == 1:
  print(paper)
elif random_list == 2:
  print(scissors)

#code for logic of rock,paper and scissors
if user_input> 2 or user_input < 0 :
  print("You typed a invalid number you lose")
elif user_input == 0 and random_list == 2:
  print("You Win")
elif random_list == 0 and user_input == 2:
  print("You lose")
elif random_list > user_input:
  print("You lose")
elif random_list < user_input:
  print("You win!")
elif user_input == random_list :
  print("It's a draw")