student_scores = input("Input a list of student scores ").split()
highest_score = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest socre in the class is {highest_score}")