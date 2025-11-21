sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

#lets initialize an empty dictionary to hold word counts
word_count = {}
#count word frequencies
for word in words:
    word = word.lower()  # convert to lowercase for uniformity
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
#display the word counts
print(word_count)
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")