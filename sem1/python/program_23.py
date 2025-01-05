import math
n1=int(input("enter starting number"))
n2=int(input("enter the ending number"))
l=[]
for i in range(n1,n2+1):
    flag=0
    num=i
    while num>0:
        digit=num%10
        if digit not in [0,2,4,6,8]:
            flag=1
            break
        num=int(num/10)
    if flag==0 and math.sqrt(i)%1==0:
        l.append(i)
print(l)
