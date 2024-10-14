str = input("enter a string")

first = str[0]
modif = first + str[1:].replace(first,"$")
print("modify string is ",modif)