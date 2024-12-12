class Student:
    def __init__(self,sid,name,age,grade):
        self.sid=sid
        self.name=name
        self.age=age
        self.grade=grade
    def assign_grade(self,gr):
        self.grade=gr
        print(f"Grade updated. grade:{self.grade}")
    def display(self):
        print(f"student id: {self.sid}")
        print(f"student name: {self.name}")
        print(f"age: {self.age}")
        print(f"grade: {self.grade}")
std1=Student(12,"rahbar",21,"A")
std1.assign_grade("A+")
std1.display()
