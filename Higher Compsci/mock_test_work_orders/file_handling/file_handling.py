import csv

student_ids = []
first_names = []
last_names = []
grades = []

def get_student_info():
    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        #skip header
        header = next(reader)

        #loop through each row
        for row in reader:
            student_ids.append(row[0])
            first_names.append(row[1])
            last_names.append(row[2])
            grades.append(row[3])
    
    return student_ids, first_names, last_names, grades

student_ids, first_names, last_names, grades = get_student_info()

#alternative method with classes

class Student:
    def __init__(self, id, first_name, last_name, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

def other_get_student_info():
    students = []
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            student = Student(
                row[0],
                row[1],
                row[2],
                row[3]
            )
            students.append(student)
    return students

students = other_get_student_info()
print(students[0].first_name)