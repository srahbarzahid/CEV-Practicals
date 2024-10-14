from collections import Counter

# Input line of text
line = "This is a test. This test is only a test."

# Split the line into words
words = line.split()
word_count = Counter(words)
print(word_count)
