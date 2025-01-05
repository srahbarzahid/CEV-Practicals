n=int(input("enter the range: "))
list=[]
for i in range(n):
    list.append(input("enter the word: "))
print(list)
first=len(list[0])
word=list[0]
for x in list:
    if first<len(x):
        first=len(x)
        word=x
print(f"longest word is {word} with length {first}")