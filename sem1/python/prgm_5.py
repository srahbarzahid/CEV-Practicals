list = []
len = int(input("enter length of list"))
print("enter a values")
for i in range(len):
    list.append(int(input()))
list2 = ['over' if x>100 else x for x in list]
print(list2)