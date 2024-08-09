    
# TODO: добавить инпут для возраста студентов.

students = [
   {"id": 1, "name": "Alice", "age": 20, "grades": [85, 92, 78]},
   {"id": 2, "name": "Bob", "age": 22, "grades": [89, 94, 90]},
   {"id": 3, "name": "Charlie", "age": 21, "grades": [80, 85, 88]},
   {"id": 4, "name": "Diana", "age": 20, "grades": [70, 75, 80]},
   {"id": 5, "name": "Eve", "age": 23, "grades": [95, 88, 91]},
   {"id": 6, "name": "Frank", "age": 22, "grades": [65, 72, 68]},
   {"id": 7, "name": "Grace", "age": 21, "grades": [88, 90, 93]},
   {"id": 8, "name": "Hannah", "age": 20, "grades": [77, 84, 79]},
   {"id": 9, "name": "Ivy", "age": 24, "grades": [82, 89, 87]},
   {"id": 10, "name": "Jack", "age": 22, "grades": [92, 85, 88]}
 ]

# MEAN (STUDENT)
def get_average_grade(student):
  return sum(student["grades"]) / len(student["grades"])

# GET AGE (AGE)
def filter_students_by_age(students, age):
    return [student for student in students if student["age"] == age]

# GET THE BEST ONE
def best_student(students):
    return max(students, key=get_average_grade)

# TOP 5
def top_5_performance(students):
    return sorted(students, key=get_average_grade, reverse=True)[:5]

# AVERAGE GRADE [0]
average_grade = get_average_grade(students[0]) # students[0] = Alice
print(f"Средний балл {students[0]['name']}: {average_grade}")

# GET STUDENTS AGED 20
studentsResult = filter_students_by_age(students, 20)
print("Студенты с возрастом 20:")
for student in studentsResult:
    print(student["name"])

# GET BEST
best_student = best_student(students)
print(f"Лучший студент: {best_student['name']} со средним баллом {get_average_grade(best_student)}")

# GET TOP 5
top_5_students = top_5_performance(students)
print("Топ 5 студентов:")
for student in top_5_students:
    print(f"{student['name']} со средними баллами {get_average_grade(student)}")