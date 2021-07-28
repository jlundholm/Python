print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You find yourself shipwrecked on a island, the trees look scary. Where do you go? Type 'Left' or 'Right'?\n").lower()

if choice1 == "left":
  choice2 = input("You come to a river, do you swim across or wait for a boat? Type 'Swim' or 'Wait'\n").lower()
  if choice2 == "swim":
    choice3 = input("As you continue on you come to a building with 3 doors. Red, Yellow, and Blue. Which color of door do you choose? Type 'Red', 'Yellow', or 'Blue'\n").lower()
    if choice3 == "yellow":
      print("(You WIN) you walk through the Yellow door and find the pirate's booty. It's gold, We know what you were thinking, pervert.")
    elif choice3 == "red":
      print("(Game Over) You walked through the Red door and into your ex's arms, this is why you never answer texts drunk.")
    else:
      print("(Game Over) You walked through the Blue door and fall into a Panter's teeth, YUM")
  else:
    print("(Game Over) You waited and waited but no boat came. You died of exposure, idiot.")

else:
  print("(Game Over) You went right and were eaten by the natives. Noice")
