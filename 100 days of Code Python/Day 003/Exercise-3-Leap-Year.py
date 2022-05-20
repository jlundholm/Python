#2016 Leap
#2020 Leap
#1999 Not Leap
#2018 Not Leap
# input "Which year do you want to check? "
year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print("Not leap year.")
elif year % 100 != 0:
    print("Leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")

      