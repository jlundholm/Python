# Rounding
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) # drops decimal
print(round(bmi)) # rounds up or down
print(round(bmi, 2)) # round to 2 decimal places

# Assignment
# +=  -=  *=  /=
score = 1
score += 1  # adds 1 to score
print(score)

# f-strings
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.")