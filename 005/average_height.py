student_heights = input("Input a list of student heights ").split()
total_students = 0
total_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
for height in student_heights:
  total_height += height

for student in student_heights:
  total_students += 1


average = round(total_height/total_students)
print(f"Average height is {average}")

# can alternatively use sum function to add up the values form the list and len to find total number of students