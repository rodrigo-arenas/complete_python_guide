
class Student:

    def __init__(self,name,school):
        self.name = name
        self.grades = school
        self.marks =[]

    def average_grade(self):
        return sum(self.marks)/len(self.marks)

#Se quiere tener un tipo especial de estudiante, que sea trabajador
#Una forma sería copiando la clase:
"""
class WorkingStudent:
    def __init__(self,name,school,salary):
        self.name = name
        self.grades = school
        self.marks =[]
        self.salary = salary

    def average_grade(self):
        return sum(self.marks)/len(self.marks)
"""
#Pero se puede heredar las propiedades de la clase Student

class WorkingStudent(Student): #Ahora es un hijo de Student
    def __init__(self,name,school,salary):
        super().__init__(name,school) #Inicializa la clase superior "Student"
        self.salary = salary
    
    #@property se usando cuando el método no requiere nada adicional a self y solo devuelve 
    #cálculos basados en self, se puede llamar como .metodo sin usar "()" y queda como propiedad
    @property 
    def weekly_salary(self):
        return self.salary*37.5


rolf = WorkingStudent('Rolf','MIT',15.4)
print(rolf.salary)

rolf.marks.append(50)
rolf.marks.append(69)

print(rolf.average_grade())

print(rolf.weekly_salary)