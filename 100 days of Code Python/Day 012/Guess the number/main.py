#Number Guessing Game Objectives:
import random
from art import logo
# Include an ASCII art logo.
print(logo)

answer = random.randint(1,100)
user_guesses_remaining = 0
is_game_over = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#cheat for testing
print(f"Psst, the correct answer is {answer}")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if user_choice == "easy":
  user_guesses_remaining = 10
else:
  user_guesses_remaining = 5


while not is_game_over:
  print(f"You have {user_guesses_remaining} attempts remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  if user_guess == answer:
    print(f"You got it! The answer was {answer}.")
    is_game_over = True
  elif user_guess > answer:
    print("Too high.")
    print("Guess again.")
  elif user_guess < answer:
    print("Too low.")
    print("Guess again.")
  user_guesses_remaining -= 1
  if user_guesses_remaining == 0:
    print("You've run out of guesses, you lose.")
    is_game_over = True





# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

