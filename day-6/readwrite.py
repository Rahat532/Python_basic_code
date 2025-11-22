# opening file reading file 
with open('day-6/sample.txt', 'r') as file:
    # content = file.read()
    content = file.readlines()
    print("File Content:")
    print(content)
    
# writing to file
with open('day-6/output.txt', 'w') as file:
    file.write("This is a sample output file.\n")
    file.writelines(["File writing successful!\n ", "This is the second line.\n"])

