first = "hello AI"
second = "BootCamp"
# concatenating strings
full_string = first + " " + second
print("Concatenated String:", full_string)

#string Slicing 
text="Artificial Intelligence"
print("Original String:", text)
print("Sliced String (0-5):", text[0:5])  # Slicing from index 0 to 5
#string Formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
# String Methods
#split(),join(),replace(),strip()
sample_text = "  Hello, World! Welcome to AI BootCamp.  "
print("Original Sample Text:", sample_text)
# Using strip() to remove leading and trailing whitespace
stripped_text = sample_text.strip()
print("Stripped Text:", stripped_text)
# Using replace() to replace a substring
replaced_text = stripped_text.replace("AI BootCamp", "Python Programming")
print("Replaced Text:", replaced_text)
# Using split() to split the string into a list of words
split_text = replaced_text.split(" ")
print("Split Text:", split_text)
# Using join() to join the list of words back into a single string  
joined_text = " ".join(split_text)
print("Joined Text:", joined_text)