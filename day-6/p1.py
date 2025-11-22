# a program to copy contents from one file to another
def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {source_file} was not found.")
    except IOError:
        print("Error: An I/O error occurred during file operations.")
# Example usage
source = 'day-6/sample.txt'
destination = 'day-6/copied_sample.txt'
copy_file_contents(source, destination)
