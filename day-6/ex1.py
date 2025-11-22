# count the word in a text file
try:
    def count_words_in_file(file_path):
      count=0
      with open(file_path,'r') as file:
        for line in file:
            words=line.split()
            count+=len(words)
      return count
except FileNotFoundError:
    print("Error: The file was not found.")
# Example usage
file_path='day-6/sample.txt'
word_count=count_words_in_file(file_path)
print(f'The number of words in the file is: {word_count}')