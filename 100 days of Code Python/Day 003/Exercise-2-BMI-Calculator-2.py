#BMI Under 18.5: underweight
#BMI Over 18.5 and below 25: Normal Weight
#BMI Over 25 and below 30: slightly overweight
#BMI Over 30 and below 35: obese
#BMI Over 35: Clinically obese
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

heightF = float(height)
weightF = float(weight)
BMI = weightF / (heightF * heightF)

if round(BMI) < 18.5:
    print (f"Your BMI is {round(BMI)}, you are underweight.")
elif (round(BMI) < 25):
    print (f"Your BMI is {round(BMI)}, you have a normal weight.")
elif (round(BMI) < 30):
    print (f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif (round(BMI) < 35):
    print (f"Your BMI is {round(BMI)}, you are obese.")
else:
    print (f"Your BMI is {round(BMI)}, you are clinically obese.")
