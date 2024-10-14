str = input("enter a string ")

if len(str) >1:
    modif = str[-1]+str[1:-1]+str[0]
else:
    modif=str
print(modif)
