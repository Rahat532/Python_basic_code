#problem is to reverse a list and remove dublicates useing sets
list1=[1,2,2,3,4,4,5]
list2=list1[::-1]
set1=set(list1)
set2=set(list2)
result=set1 | set2
print(f"no dublicates and reversed list is : {result}")