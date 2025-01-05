l=int(input("enter the length of square"))
s_area=lambda a:a*a
l1=int(input("enter the length of rectangle"))
w1=int(input("enter the width of rectangle"))
r_area= lambda l1,w:l1*w
b=int(input("enter the base of triangle"))
h=int(input("enter the height of triangle"))
t_area=lambda b,h:0.5*b*h
print(f"area of square:{s_area(l)}")
print(f"area of rectangle:{r_area(l1,w1)}")
print(f"area of triangle:{t_area(b,h)}")