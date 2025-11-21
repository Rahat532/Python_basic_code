# this is here for name variable 
integer_var =12
string_var ="hello AI"
float_var = 12.34 
boolean_var = True
list_var = [1, 2, 3, 4, 5, " six"]
dict_var = {"name": "Alice", "age": 30}
tuple_var = (10, 20, 30)

# printing all variable types
print("Integer Variable:", integer_var)
print("Float variable:", float_var+integer_var)
print("String variable: " + string_var + " BootCamp")
print("Boolean variable:", boolean_var)
list_var.append(string_var)
new_list = list_var
for item in new_list:
    print(item)
print("Dictionary variable:", dict_var["name"])
print("Tuple variable:", tuple_var)