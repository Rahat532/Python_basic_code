try:
    with open('day-6/sample.txt', 'r') as file:
        content = file.read()
        print("File content successfully read:")
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")