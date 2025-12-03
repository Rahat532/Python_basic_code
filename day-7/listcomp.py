# lets talk about list comprehensions
squares = [x**2 for x in range(10)]
print(squares)
# filtering even squares
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
# converting to uppercase
words = ['hello', 'world', 'python', 'is', 'fun']
upper_words = [word.upper() for word in words]
print(upper_words)

#lambda Functions
add = lambda x, y: x + y # Dont need def keyword
result = add(5, 3)
print(result)

