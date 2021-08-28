############DEBUGGING#####################

# Describe Problem
# The fuction should print "You got it" when i = 20
# The loop will break when it reaches 20, so 20 never prints
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# the random numbers are 1 - 6, but the list is 0 - 5
# so when it chooses 6 you'll get out of range
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer
# Gen Z never runs as it's great than 94 which gen z would not be.

# year = int(input("What's your year of birth? "))
# if year < 1981:
#   print("You are Gen X.")
# elif year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
#age = int(input("How old are you? "))
#if age > 18:
#  print(f"You can drive at age {age}.")

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])