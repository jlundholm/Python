# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
student_total = 0
student_sum = 0
average = 0

for heights in student_heights:
  student_total += 1
  student_sum += heights

average = round(student_sum / student_total, 0)

print(int(average))