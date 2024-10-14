import os.path

file = input("enter a file name ")
exte = file.split(".")[-1]
print(f"The extension of the file is '{exte}'")

#another method

name,extension = os.path.splitext(file)
print("The extension of the file is",extension[1:])