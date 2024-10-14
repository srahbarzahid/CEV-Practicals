list1 = input("enter the numbers using spaces").split()
list2 = input("enter the numbers using spaces").split()

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

length = len(list1) == len(list2)
sum = sum(list1) == sum(list2)
common = set(list1) & set(list2)

print(f"is the length of these two list are equal :{length}")
print(f"is the sum of these 2 lists are equal: {sum}")
print(f"common variable is {common}")

