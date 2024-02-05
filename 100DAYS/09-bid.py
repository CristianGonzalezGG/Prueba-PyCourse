# diccionarios
# programming_diccionary= {
#     "Bug": "Funtion of a bug is when an error occurs in the code",
#     "Mel": "sapo",    
# }
# imprimiento items de el diccionario
# print(programming_diccionary["Bug"])

# adding items
# programming_diccionary["Tiki"]= "szs"
# print(programming_diccionary["Tiki"])
# editing a value or item
# programming_diccionary["Bug"] = "I changed the text and take off"

# for thing in programming_diccionary:
#     print(f'{thing}: ')
#     print(programming_diccionary[thing])


#EXERCISE

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
students_grades = {}
for key in student_scores:
    if student_scores[key] <= 70:
        print("Fail")
        status = "Fail"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        print("Acceptable")
        status = "Acceptable"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        print("Exceeds Expectations")
        status = "Exceeds Expectations"
    elif student_scores[key] >= 91 and student_scores[key] <= 100:
        print("Outstanding")
        status = "Outstanding"
    students_grades[key] = status

for student, grade in students_grades.items():
    print(student)
    print(grade)