class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
    def per(self):
        return 2*(self.length+self.width)
    def compare(self,other):
        if self.area()>other.area():
            print(f"area of rectangle1 is greater:{self.area()}")
        elif other.area()>self.area():
            print(f"area of rectangle2 is greater:{other.area()}")
        else:
            print("area of rectangles are equal")

l1=int(input("enter the length: "))
w1=int(input("enter the width: "))

l2=int(input("enter the length2:"))
w2=int(input("enter the width2: "))

r1=Rectangle(l1,w1)
print(f"area of rectangle1:{r1.area()}")
print(f"perimeter of rectangle1:{r1.per()}")
r2=Rectangle(l2,w2)
print(f"area of rectangle2:{r2.area()}")
print(f"perimter of rectangle2:{r2.per()}")
r1.compare(r2)