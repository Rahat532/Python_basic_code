def is_palindrome(text):
 text=" ".join(chr.lower() for chr in text if chr.isalnum())
 return text==text[::-1]
# Example usage
sample_text=input("Enter a string to check for palindrome: ")
if is_palindrome(sample_text):
    print(f'"{sample_text}" is a palindrome.')
else:
    print(f'"{sample_text}" is not a palindrome.')