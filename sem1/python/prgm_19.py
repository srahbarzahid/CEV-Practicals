dict1 = {}
dict2 = {}
n1 = int(input("enter the length of 1st dictionary "))

for i in range(n1):
    key = input("enter the key ")
    value = input("enter the value ")
    dict1[key] = value
n2 = int(input("enter the length of 2nd dictionary "))
for i in range(n2):
    key = input("enter key ")
    value = input("enter the value ")
    dict2[key]=value

dict1.update(dict2)
print(dict1)