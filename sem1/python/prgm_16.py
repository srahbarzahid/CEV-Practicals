str1 = input("enter a first string ")
str2 = input("enter the 2nd string ")

res = str2[0]+str1[1:] +" "+ str1[0]+str2[1:]
print(res)