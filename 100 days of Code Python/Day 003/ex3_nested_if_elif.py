print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    if age >= 18:
        print("Please pay $12 to ride.")
    elif age >= 12:
        print("Please pay $7 to ride.")
    else:
        print("please pay $5 to ride.")
else:
    print("Sorry you have to grow taller before you can ride.")
