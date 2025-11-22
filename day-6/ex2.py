def write_items_to_file(filename, items):
    """Writes a list of items to a file, each on a new line."""
    with open(filename, 'w') as file:
        for item in items:
            file.write(f"{item}\n")
            
def read_items_from_file(filename):
    """Reads items from a file and returns them as a list."""
    try:
        with open(filename, 'r') as file:
           items=file.readlines()
           print("items in the files are:")
           for item in items:
               print(item.strip())
    except FileNotFoundError:
      print(f"This {filename} file is not found.")
      return []
    return items

fruits = ['apple', 'banana', 'cherry', 'date']
file_name = 'day-6/fruits.txt'
write_items_to_file(file_name, fruits)
read_items_from_file(file_name)
