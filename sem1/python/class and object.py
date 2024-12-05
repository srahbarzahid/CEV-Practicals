class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(f"ram of the computer is {self.cpu}")
        print(f"the ram is {self.ram}")
object1= Computer("Ryzen 5","32GB")
object1.config()

#student class and objects

class Student:
    def __init__(self,name,course,age):
        self.name=name
        self.age=age
        self.course=course
    def config(self):
        return f"name: {self.name}, age:{self.age}, course: {self.course}"
std1=Student("rahbar","MCA",21)
print(std1.config())