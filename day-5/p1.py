# count  number of vowels in string 
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
# Example usage
sample_string = input("Enter a string to count vowels: ")
vowel_count = count_vowels(sample_string)
print(f'The number of vowels in the string is: {vowel_count}')