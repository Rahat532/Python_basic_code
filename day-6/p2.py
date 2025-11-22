# write a program to count specific word in a text file
def count_specific_word(file_path,target_word):
    count=0
    try:
        with open(file_path,'r')as file:
            for line in file:
                Words=line.split()
                for word in Words:
                    if word.lower()==target_word.lower():
                        count+=1
    except FileNotFoundError:
        print(f"Error: The {file_path} file was not found.")
    return count
# Example usage
file_path='day-6/sample.txt'
target_word='the'
word_count=count_specific_word(file_path,target_word)
print(f"The word '{target_word}' appears {word_count} times in the file.")