
height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in lbs: "))

bmi = round((weight / (height **2)) * 703)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underwight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you area clinically obese.")