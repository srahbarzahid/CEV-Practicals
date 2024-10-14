list1 = input("enter the list1 colors ").split()
list2 = input("enter a list2 colors ").split()
dif = set(list1) - set(list2)
print(dif)