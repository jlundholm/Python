
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name1 = name1.lower()
name2 = name2.lower()

name1True = name1.count("t") +  name1.count("r") + name1.count("u") + name1.count("e")
name2True = name2.count("t") +  name2.count("r") + name2.count("u") + name2.count("e")
scoreTrue = name1True + name2True

name1Love = name1.count("l") +  name1.count("o") + name1.count("v") + name1.count("e")
name2Love = name2.count("l") +  name2.count("o") + name2.count("v") + name2.count("e")
scoreLove = name1Love + name2Love

score = str(scoreTrue) + str(scoreLove)

if int(score) < 10 or int(score) > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

#Instructor Code
#combined_names = name1 + name2
#lower_names = combined_names.lower()
#t = lower_names.count("t")
#r = lower_names.count("r")
#u = lower_names.count("u")
#e = lower_names.count("e")
#first_digit = t + r + u + e

#l = lower_names.count("l")
#o = lower_names.count("o")
#v = lower_names.count("v")
#e = lower_names.count("e")
#second_digit = l + o + v + e

#score = int(str(first_digit) + str(second_digit))

#if (score < 10) or (score > 90):
#  print(f"Your score is {score}, you go together like coke and mentos.")
#elif (score >= 40) and (score <= 50):
#  print(f"Your score is {score}, you are alright together.")
#else:
#  print(f"Your score is {score}.")
