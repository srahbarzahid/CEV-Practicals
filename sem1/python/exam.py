import math
# y1=int(input("enter a year"))
# y2=int(input("ending year"))
# for i in range(y1,y2+1):
#     if i%400==0 or (i%4==0 and i%100!=0):
#         print(i)

# list = [1,-2,4,-5,-6,9,7]
# l1=[x for x in list if x>0]
# print(l1)
# n= int(input("enter the range"))
# sqr=[x*x for x in range(1,n+1)]
# print(sqr)
# word="good morning"
# vowels=[x for x in word if x.lower() in "aeiou"]
# print(vowels)
# ordinal=[ord(x) for x in word]
# print(ordinal)

# word = input("enter a word").split()
# count={}
# for x in word:
#     if x.lower() in count:
#         count[x]+=1
#     else:
#         count[x]=1
# print(count)


# no=[1020,33,456,231,11]
# list=['over' if x>100 else x for x in no]
# print(list)


# names=["rahbar","amal","ameen","ramzy"]
# count=0
# for x in names:
#     for y in x:
#         if y.lower() == "a":
#             count+=1
# print(f"count of a is:{count}")


# l1=[1,2,3,4,5]
# l2=[2,4,1,4,5]
# sum1=sum(l1)
# sum2=sum(l2)
# print(f"sum1:{sum1}")
# print(f"sum2:{sum2}")
# if len(l1)==len(l2):
#      print("length of two lists are equal")
# else:
#     print("length are not equal")
# if sum(l1)==sum(l2):
#     print(f"sums are equal")
# else:
#     print("sums are not equal")


# str=input("enter a string: ")
# print(str[-1]+str[1:-1]+str[0])


# r=int(input("enter the radius"))
# area= math.pi*r*r
# print(f"area:{area}")


# file=input("enter a file name with extension").split('.')
# print(f"extension is: {file[-1]}")


# n=int(input("enter the length of color"))
# color=[]
# for i in range(n):
#     color.append(input("enter the color: "))
# print(f"first color is:{color[0]}")
# print("last color is",color[-1])


# n=input("enter an integer")
# res=int(n)+int(n*2)+int(n*3)
# print(f"n+nn+nnn: {res}")


# l1=['yellow',"orange","blue"]
# l2=["blue","red","white"]
# for x in l1:
#     if x not in l2:
#         print(x)


# str1="amal"
# str2="neeradh"
# res= str2[0]+str1[1:]+" "+str1[0]+str2[1:]
# print(res)


# dict1={"name":"rahbar",
#        "age":21,
#        "course":"MCA",
#        "college":"cev"
#        }
# asc=dict(sorted(dict1.items()))
# print(f"Ascending order: {asc}")
# print(f"descending order: {dict(sorted(dict1.items(),reverse=True))}")


# fruits={
#     "apple":4,
#     "banana":5,
#     "orange":6
# }
# veg={"tomato":10,"carrot":2,"onion":19}
# print(fruits,veg)
# c=fruits.copy()
# c.update(veg)
# print("merged: ",c)


# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# while b!=0:
#     r=a%b
#     a=b
#     b=r
# print(f"gcd of two numbers is: {a}")


# n=int(input("enter the range"))
# l1=[]
# for i in range(n):
#     l1.append(int(input("enter the number: ")))
# pos=[x for x in l1 if x%2!=0]
# print(pos)



# n=int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"factorial : {fact}")

# n1=0
# n2=1
# n = int(input("enter the range"))
# print(n1)
# print(n2)
# for i in range(2,n):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3)


# n=int(input("enter the range"))
# l=[]
# sum=0
# for i in range(n):
#     l.append(int(input("enter a number: ")))
# print(l)
# for x in l:
#     sum+=x
# print("sum:",sum)


# n1=int(input("enter starting number"))
# n2=int(input("enter the ending number"))
# l=[]
# for i in range(n1,n2+1):
#     flag=0
#     num=i
#     while num>0:
#         digit=num%10
#         if digit not in [0,2,4,6,8]:
#             flag=1
#             break
#         num=int(num/10)
#     if flag==0 and math.sqrt(i)%1==0:
#         l.append(i)
# print(l)


# n=int(input("enter a range: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i*j," ",end="")
#     print()


# word=input("enter a word: ")
# count=0
# for x in word:
#     if x!=" ":
#         count+=1
# print(f"count of the word is:{count}")


# word=input("enter a word")
# if word.endswith("ing"):
#     word+="ly"
# else:
#     word+="ing"
# print(f"updated word is:{word}")


# n=int(input("enter the range: "))
# list=[]
# for i in range(n):
#     list.append(input("enter the word: "))
# print(list)
# first=len(list[0])
# word=list[0]
# for x in list:
#     if first<len(x):
#         first=len(x)
#         word=x
# print(f"longest word is {word} with length {first}")


# n=int(input("enter the range"))
# for i in range(n):
#     for j in range(i+1):
#         print("*"," ",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*"," ",end="")
#     print()



# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# l=int(input("enter the length of square"))
# s_area=lambda a:a*a
# l1=int(input("enter the length of rectangle"))
# w1=int(input("enter the width of rectangle"))
# r_area= lambda l1,w:l1*w
# b=int(input("enter the base of triangle"))
# h=int(input("enter the height of triangle"))
# t_area=lambda b,h:0.5*b*h
# print(f"area of square:{s_area(l)}")
# print(f"area of rectangle:{r_area(l1,w1)}")
# print(f"area of triangle:{t_area(b,h)}")


# class Rectangle:
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def area(self):
#         return self.length*self.width
#     def per(self):
#         return 2*(self.length+self.width)
#     def compare(self,other):
#         if self.area()>other.area():
#             print(f"area of rectangle1 is greater:{self.area()}")
#         elif other.area()>self.area():
#             print(f"area of rectangle2 is greater:{other.area()}")
#         else:
#             print("area of rectangles are aequal")
#
# l1=int(input("enter the length: "))
# w1=int(input("enter the width: "))
#
# l2=int(input("enter the length2:"))
# w2=int(input("enter the width2: "))
#
# r1=Rectangle(l1,w1)
# print(f"area of rectangle1:{r1.area()}")
# print(f"perimeter of rectangle1:{r1.per()}")
# r2=Rectangle(l2,w2)
# print(f"area of rectangle2:{r2.area()}")
# print(f"perimter of rectangle2:{r2.per()}")
# r1.compare(r2)


# class Bank:
#     def __init__(self,accno,name,type,bal):
#         self.accno=accno
#         self.name=name
#         self.type=type
#         self.bal=bal
#     def deposit(self,amt):
#         if amt<0:
#             print("amount should be positive")
#         else:
#             self.bal+=amt
#     def withdraw(self,amt):
#         if amt>self.bal:
#             print("insufficient balance")
#         elif amt<0:
#             print("it should be positive")
#         else:
#             self.bal-=amt
#     def display(self):
#         print(f"Account No:{self.accno}")
#         print(f"Name:{self.name}")
#         print(f"Type:{self.type}")
#         print(f"Balance:{self.bal}")
#
# user1=Bank(23344,"amal","savings",3400)
# while True:
#     print("1.Deposit\n2.Withdraw\n3.Display\n4.Exit\n")
#     opt=int(input("enter the option:"))
#     if opt==1:
#         amt=int(input("enter the amount: "))
#         user1.deposit(amt)
#     elif opt==2:
#         amt = int(input("enter the amount: "))
#         user1.withdraw(amt)
#     elif opt==3:
#         user1.display()
#     elif opt==4:
#         exit(0)
#     else:
#         print("invalid option")


# class Publisher:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"Publisher: {self.name}")
# class Book(Publisher):
#     def __init__(self,name,title,author):
#         super().__init__(name)
#         self.title=title
#         self.author=author
#     def display(self):
#         super().display()
#         print(f"Title:{self.title}")
#         print(f"Author:{self.author}")
# class Python(Book):
#     def __init__(self,name,title,author,price,no_pages):
#         super().__init__(name,title,author)
#         self.price=price
#         self.no_pages=no_pages
#     def display(self):
#         super().display()
#         print(f"Price:{self.price}")
#         print(f"No of Pages:{self.no_pages}")
# book1=Python("Dc","aadujeevitham","basheer",899,345)
# book1.display()


# class Rectangle:
#     def __init__(self,l,w):
#         self.__len=l
#         self.__wid=w
#     def area(self):
#         return self.__len*self.__wid
#     def __lt__(self,other):
#         if self.area()<other.area():
#             return True
#         else:
#             return False
# r1=Rectangle(3,5)
# r2=Rectangle(5,8)
# print(f"area of rectangle1:{r1.area()}")
# print(f"area of rectangle2 : {r2.area()}")
# if r1<r2:
#     print("area of rectangle2 is greater",r2.area())
# else:
#     print("area of rectangle 1 is greater",r1.area())



class Time:
    def __init__(self,h,m,s):
        self.hour=h
        self.min=m
        self.sec=s
    def display(self):
        print("Hour:Minute:Second")
        print(f"{self.hour}:{self.min}:{self.sec}")
    def __add__(self,other):
        h=self.hour+other.hour
        m=self.min+other.min
        s=self.sec+other.sec

        if s>=60:
            m+=int(s/60)
            s=s%60
        elif m>=60:
            h+=int(m/60)
            m=m%60
        t3=Time(h,m,s)
        return t3

t1=Time(3,45,56)
t2=Time(4,50,40)
t3=t1+t2
t3.display()
