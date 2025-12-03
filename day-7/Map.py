from functools import reduce
# let's use map(), filter() and reduce()
numbers = [1, 2, 3, 4, 5]
# using map to square each number
squared= map(lambda x: x**2, numbers)
print(list(squared))

#filter to get even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

# reduce to get the product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)