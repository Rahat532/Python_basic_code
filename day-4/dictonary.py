# Dictionaries in Python
person = {"name": "Alice", "age": 30, "city": "New York","grade": "A"}
# Accessing dictionary elements
print("Name:", person["name"])  # Accessing value by key    
for key, value in person.items():
    print(f"{key}: {value}")

# Modifying dictionary elements
person["age"] = 31  # Updating age
person["grade"] = "A+"  # Updating grade
person["Department"] = "Engineering"  # Adding new key-value pair
print("Updated Person Dictionary:", person)
# Removing elements from dictionary
del person["city"]  # Removing city
print("After deleting city:", person)
person.pop("grade")  # Removing grade using pop
print("After popping grade:", person)