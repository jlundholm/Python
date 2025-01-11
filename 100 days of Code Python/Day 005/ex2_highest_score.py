student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# built in sum for lists
total_exam_score = sum(student_scores)
print(total_exam_score)

# add all scores with for loop
sum = 0
for score in student_scores:
    sum += score
print(sum)

# pull highest score from the list
high = 0
for highest in student_scores:
    if highest > high:
        high = highest
print(high)

# using built-in function
print(max(student_scores))
