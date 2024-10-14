my_dict = {}
n = int(input("enter the length "))
for i in range(n):
    key = input("enter key ")
    value = input("enter value ")
    my_dict[key] = value

print("sorted =",sorted(my_dict.items()))
print("unsorted =",sorted(my_dict.items(), reverse= True))