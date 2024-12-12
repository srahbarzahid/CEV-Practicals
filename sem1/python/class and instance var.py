class Student:
    tutor="Bind Mam"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def studentDet(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"tutor:{__class__.tutor}")
std1= Student("rahbar",21)
std1.studentDet()
