# checking conditions
num = 10
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")

#nested conditions
age = 25
if age > 18:
     if age< 30:
         print("Young Adult")
     else:
         print("Adult")
else:
    print("Minor")

#looping through a list and loop concepts
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print("I like", item)

#loop with the range function
for i in range(5):
    print("Iteration:", i)
    
#while loop example
count = 5
while count > 0:
    print("Count:", count)
    count -= 1 
    
#using break and continue
for i in range(10):
    if i == 5:
        print("Breaking the loop at", i)
        break
    if i % 2 == 0:
        continue
    print("Odd number:", i)
