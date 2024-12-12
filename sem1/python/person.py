class Person:
     def __init__(self,name,age):
         self.name=name
         self.age=age
n1=input("enter name of person1 ")
a1=int(input("enter the age of person1 "))
p1=Person(n1,a1)

n2=input("enter the name of the person2 ")
a2=int(input("enter the age of person2 "))
p2=Person(n2,a2)

if p1.age >p2.age:
    print(f"{p1.name} is elder")
elif p2.age>p1.age:
    print(f"{p2.name} is elder")
else:
    print(f"ages of {p1.name} and {p2.name} are equal")