person={"name":"John","age":25,"city":"New York"}
for key,value in person.items():
    print(f"{key}: {value}")
print("Modifying dictionary elements:")
# Modifying dictionary elements
person["age"]=26
for key,value in person.items():
    print(f"{key}: {value}")
print("Adding new key-value pair:")
person["profession"]="Engineer"
for key,value in person.items():
    print(f"{key}: {value}")
print("Removing elements from dictionary:")
if "city" in person:
    del person["city"]
for key,value in person.items():
    print(f"{key}: {value}")