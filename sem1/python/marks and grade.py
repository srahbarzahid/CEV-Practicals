class Student:
    def __init__(self,name,rollNo,marks):
        self.name=name
        self.rollNo=rollNo
        self.marks=marks
    def calcPerc(self):
        total=sum(self.marks)
        paper=len(self.marks)
        return (total/(100*paper))*100
    def grade(self,perc):
        if perc>=85:
            return "S"
        elif perc>=75:
            return "A"
        elif perc>=65:
            return "B"
        elif perc>=55:
            return "C"
        elif perc>=50:
            return "D"
        else:
            return "FAIL"
    def stdDetails(self):
        perc= self.calcPerc()
        grade=self.grade(perc)

        print()
        print(f"Roll No:{self.rollNo}")
        print(f"Name:{self.name}")
        print(f"Marks:{self.marks}")
        print(f"Percentage:{round(perc,2)}")
        print(f"Grade:{grade}")

name=input("enter the name: ")
roll=int(input("enter your Roll no: "))
sn=int(input("how many subjects you have: "))
print("enter your subjects")
marks=[]
for i in range(sn):
    marks.append(int(input(f"enter the mark subject{i+1}: ")))
std1=Student(name,roll,marks)
std1.stdDetails()