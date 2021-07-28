# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#heightEx = float(height)
#weightEx = float(weight)
#print(weightEx / (heightEx * heightEx))

bmi = float(weight) / float(height) **2
print(int(bmi))