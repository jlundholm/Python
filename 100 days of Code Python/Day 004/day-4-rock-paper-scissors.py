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
# create list
rules =[rock, paper, scissors]

# input from human player
player1 = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# find length of list and randomly select computer choice
num_items = len(rules)
computer = random.randint(0, num_items - 1)

# logic to print player choice
if player1 == '0':
  print(rock)
  print("Computer chose:\n")
elif player1 == '1':
  print(paper)
  print("Computer chose:\n")
elif player1 == '2':
  print(scissors)
  print("Computer chose:\n")
else:
  print("You typed an invalid number, you lose!")
  exit()

# Print computer choice
print(rules[computer])

#logic for who wins
if player1 == '0' and computer == 2:
  print("You win!")
elif player1 == '0' and computer == 0:
  print("It's a draw")
elif player1 =='1' and computer == 0:
  print("You win!")
elif player1 == '1' and computer == 1:
  print("It's a draw")
elif player1 =='2' and computer == 1:
  print("You win!")
elif player1 == '2' and computer == 2:
  print("It's a draw")
else:
  print("You lose")