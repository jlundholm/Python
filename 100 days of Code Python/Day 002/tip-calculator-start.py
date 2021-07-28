#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
totalBill = input("What was the total bill? ")
percentage = input("What percentange tip would you like to give? 10, 12, or 15 ")
split = input("How many people to split the bill? ")

totalBillInt = int(totalBill)
percentageInt = int(percentage)
splitInt = int(split)
ten = 1.00
twelve = 1.12
fifteen = 1.15

if percentageInt == 10:
  result = (totalBillInt * ten / splitInt)

if percentageInt == 12:
  result = (totalBillInt * twelve / splitInt)
  
if percentageInt == 15:
  result = (totalBillInt * fifteen / splitInt)

print("Each person should pay: $" + str(round(result, 2)))