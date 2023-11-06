# creating a new dictionary from the values in an existing list
# syntax: new_dict = {new_key:new_value for item in list}

# creating a new dictionary from the values in an existing dictionary
# syntax: new_dict = {new_key:new_value for (key,value) in dict.items()}

# conditional dictionary comprehension
# syntax: new_dict = {new_key:new_value for (key,value) in dict.items() if test}

from random import randint
students = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# generating a random score for students
student_scores ={student:randint(1, 100) for student in students}
print(student_scores)

# only students who have passed i.e., people who have scored 60 and above
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)