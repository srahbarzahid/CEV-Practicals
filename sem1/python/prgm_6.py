list = ["rahbar","amal","nihad"]
count = 0
for x in list:
    # print(x)
    count += x.lower().count("a")
print(f"count of 'a' is {count}")