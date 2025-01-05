n=int(input("enter the range"))
l=[]
sum=0
for i in range(n):
    l.append(int(input("enter a number: ")))
print(l)
for x in l:
    sum+=x
print("sum:",sum)