# Tuples in Python
colour= ("red", "green", "blue")  # This is a tuple
single_item=("yellow",)  # Tuple with single item needs a comma
print("Tuple:", colour)
print("First item:", colour[0])
print("Single item tuple:", single_item)
# important note about tuples
""" 
Tuples are immutable, meaning once created, their elements cannot be changed, added, or removed.
For example, you cannot do the following operations on a tuple: 
colour[0] = "purple"  # This will raise an error
colour.append("purple")  # This will raise an error

"""