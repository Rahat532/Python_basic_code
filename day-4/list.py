# lets learn about lists in python
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry", "date"]
mixed = [1, "hello", 3.14, True, [5, 6, 7]]
# printing the lists
print("Numbers List:", numbers[2])#accessing 3rd element
print("Fruits List:", fruits[-1])#accessing last element via negative indexing
print("Mixed List:", mixed[1:3])#slicing first three elements
#modifying list
numbers.append(60)#adding element at the end
fruits.remove("banana")#removing an element
print(fruits)
fruits.insert(1, "blueberry")#inserting at specific position
print(fruits)
del fruits[0]#deleting an element
print(fruits)
fruits.pop()#removing last element
print(fruits)
mixed[1] = "world"#changing an element
print(mixed)
