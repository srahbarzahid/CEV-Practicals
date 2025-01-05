word=input("enter a word")
if word.endswith("ing"):
    word+="ly"
else:
    word+="ing"
print(f"updated word is:{word}")
