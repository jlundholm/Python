import random
import art
from game_data import data
from replit import clear

score = 0
is_game_over = False

# Get random data from list
getRandomA = random.randint(0,len(data)-1)
A = data[getRandomA]
aCount = A['follower_count']


getRandomB = random.randint(0,len(data)-1)
B = data[getRandomB]
bCount = B['follower_count']


print(art.logo)
print(f"Compare A: {A['name']} a {A['description']}, from {A['country']}.")
# show follower cheat
#print(f"Cheat fc {A['follower_count']} aCount {aCount}")
print(art.vs)
print(f"Against B: {B['name']} a {B['description']}, from {B['country']}.")
# show follower cheat
#print(f"Cheat fc {B['follower_count']} bCount {bCount}")
userChoice = input("Who has more followers? Type 'A' or 'B': ")

def game_over():
  global is_game_over
  is_game_over = True
  clear()
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {score}")

def playGame():
  global score
  global A
  global B
  global userChoice
  global aCount
  global bCount
  score += 1
  clear()
  A = B
  aCount = A['follower_count']
  getRandomB = random.randint(0,len(data)-1)
  B = data[getRandomB]
  bCount = B['follower_count']
  print(art.logo)
  print(f"you're right! Current score: {score}.")
  print(f"Compare A: {A['name']} a {A['description']}, from {A['country']}.")
  # show follower cheat
  #print(f"Cheat fc {A['follower_count']} aCount {aCount}")
  print(art.vs)
  print(f"Against B: {B['name']} a {B['description']}, from {B['country']}.")
  # show follower cheat
  #print(f"Cheat fc {B['follower_count']} bCount {bCount}")
  userChoice = input("Who has more followers? Type 'A' or 'B': ")


while not is_game_over:
  largerCount = aCount > bCount
  if largerCount == True and userChoice == 'B':
    game_over()
  elif largerCount == False and userChoice == 'A':
    game_over()
  else:
    playGame()




