your_age = int(input("How old are you?\n"))
def life_in_weeks(age):
    time_left = (90 - age) * 52
    print(f"You have {time_left} weeks left.")

life_in_weeks(your_age)
