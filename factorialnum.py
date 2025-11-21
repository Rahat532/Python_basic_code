num=int(input("Enter a number: "))
if num<0:
    print("Factorial not defined for negative numbers")
else:
    res =1
    for i in range(1,num+1):
        res=res*i
    print(f"The factorial of {num} is {res}")