#lets create a list and find the largest number in it
num=int(input("Enter the number of elements in the list: "))
numbers=[]
while num>0:
    element=int(input("Enter a number: "))
    numbers.append(element)
    num-=1
print(f"Here is the list you entered: {numbers}")
#lets find the largest number
largest=numbers[0]
for i in numbers:
    if i>largest: #comparing each number with the current largest number
        largest=i
print(f"The largest number in the list is: {largest}")