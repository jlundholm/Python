# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightF = float(height)
weightF = float(weight)
BMI = weightF / (heightF * heightF)
print(int(BMI))