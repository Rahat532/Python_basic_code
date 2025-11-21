num_set = {1, 2, 3, 4, 5}  # This is a set
empty_set = set()  # Correct way to create an empty set
print(num_set)
num_set.add(6)  # Adding an element to the set
print("After adding 6:", num_set)
num_set.remove(3)  # Removing an element from the set
print("After removing 3:", num_set)
# set operations
another_set = {4, 5, 6, 7, 8}
union_set = num_set.union(another_set)
print("Union of sets:", union_set)
intersection_set = num_set.intersection(another_set)
print("Intersection of sets:", intersection_set)    
difference_set = num_set.difference(another_set)
print("Difference of sets (num_set - another_set):", difference_set)  

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union= set1 | set2
print("Union using | operator:", union)
intersection= set1 & set2
print("Intersection using & operator:", intersection)   
defference= set1 - set2
print("Difference using - operator (set1 - set2):", defference)  
