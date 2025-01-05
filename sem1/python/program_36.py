class Rectangle:
    def __init__(self,l,w):
        self.__len=l
        self.__wid=w
    def area(self):
        return self.__len*self.__wid
    def __lt__(self,other):
        if self.area()<other.area():
            return True
        else:
            return False
r1=Rectangle(3,5)
r2=Rectangle(5,8)
print(f"area of rectangle1:{r1.area()}")
print(f"area of rectangle2 : {r2.area()}")
if r1<r2:
    print("area of rectangle2 is greater",r2.area())
else:
    print("area of rectangle 1 is greater",r1.area())