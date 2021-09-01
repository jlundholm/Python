import random
import art
from game_data import data

score = 0

# Turn this into a function
getRandomA = random.randint(0,len(data)-1)
getRandomB = random.randint(0,len(data)-1)
A = data[getRandomA]
B = data[getRandomB]
C = 0

print(art.logo)
print(f"Compare A: {A['name']} a {A['description']}, from {A['country']}.")
print(art.vs)
print(f"Against B: {B['name']} a {B['description']}, from {B['country']}.")
#input("Who has more followers? Type 'A' or 'B': ")