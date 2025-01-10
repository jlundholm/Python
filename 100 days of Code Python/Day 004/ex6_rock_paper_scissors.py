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
signals = [rock, paper, scissors]
comp_choice = random.choice(signals)
# print(comp_choice)

choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(type(choice))

if choice == 0 and comp_choice == scissors:
    print(rock)
    print(f"Computer Chose:\n{comp_choice}")
    print("You Win!")
elif choice == 0 and comp_choice == rock:
    print(rock)
    print(f"Computer Chose:\n{comp_choice}")
    print("Draw")
elif choice == 0 and comp_choice == paper:
    print(rock)
    print(f"Computer Chose:\n{comp_choice}")
    print("You Lose!")
elif choice == 1 and comp_choice == rock:
    print(paper)
    print(f"Computer Chose:\n{comp_choice}")
    print("You Win!")
elif choice == 1 and comp_choice == paper:
    print(paper)
    print(f"Computer Chose:\n{comp_choice}")
    print("Draw")
elif choice == 1 and comp_choice == scissors:
    print(paper)
    print(f"Computer Chose:\n{comp_choice}")
    print("You Lose!")
elif choice == 2 and comp_choice == paper:
    print(scissors)
    print(f"Computer Chose:\n{comp_choice}")
    print("You Win!")
elif choice == 2 and comp_choice == scissors:
    print(scissors)
    print(f"Computer Chose:\n{comp_choice}")
    print("Draw")
elif  choice == 2 and comp_choice == rock:
    print(scissors)
    print(f"Computer Chose:\n{comp_choice}")
    print("You Lose!")
else:
    print("You typed an invalid number. You lose!")
