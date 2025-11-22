import re
# some regular expression operations in Python
text = "The rain in Spain stays mainly in the plain."
# search() function, findall() ,sub()
match = re.search(r"ain", text)
if match:
    print("Found:", match.group())
else:
    print("No match found.")
all_matches = re.findall(r"ain", text)
print("All matches of 'ain':", all_matches)
replaced_text = re.sub(r"ain", "X", text)
print("Replaced Text:", replaced_text)
