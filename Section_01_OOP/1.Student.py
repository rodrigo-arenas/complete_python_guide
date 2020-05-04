class Student:

    def __init__(self,new_name,new_grade):
        self.name = new_name
        self.grades = new_grade

    def average_grade(self):
        return sum(self.grades)/len(self.grades)


student_one = Student('Alex',[90,54,32,27])

print(student_one.average_grade())
print(Student.average_grade(student_one))