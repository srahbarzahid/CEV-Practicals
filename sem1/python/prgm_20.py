list1 = input("enter the numbers").split()
list1 = [int(x) for x in list1]
list2 = [x for x in list1 if x%2!=0]
print(list2)