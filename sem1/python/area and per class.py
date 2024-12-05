class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def per(self):
        return 2*(self.length+self.breadth)

l1=int(input("enter the length of rect1: "))
b1=int(input("enter the breadth of rect1: "))

r1= Rectangle(l1,b1)
print(f"area of the rectangle:{r1.area()}")
print(f"perimeter of the rectangle:{r1.per()}")
print(Rectangle.length)
l2=int(input("enter the length of rectangle2:"))
b2=int(input("enter the breadth of rectangle2:"))
r2=Rectangle(l2,b2)
print(f"area of the rectangle2:{r2.area()}")
print(f"perimeter of the rectangle2:{r2.area()}")
print()
a1=r1.area()
a2=r2.area()
if a1 > a2:
    print("area of the rectangle1 is higher")
elif a1==a2:
    print("area of the rectangles are equal")
else:
    print("area of the rectangle2 is higher")
