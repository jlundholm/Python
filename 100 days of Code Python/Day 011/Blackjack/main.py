############### Blackjack Project #####################
from art import logo
import random
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
  print(logo)
  # pulling 2 cards for both the user and computer
  for char in range(1, 3):
    user_cards.append(random.choice(cards))
  for char in range(1, 3):
    computer_cards.append(random.choice(cards))

  
  print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
  print(f"Computer's first card: {computer_cards[0]}")
  print(f"*testing: computer current score: {calculate_score(computer_cards)}")
  
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
def calculate_score(score):
  sum(score)
  if len(user_cards) == 2 and sum(score) == 21:
    return 0
  else:
    return sum(score)


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == "y":
  deal_card()






#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

