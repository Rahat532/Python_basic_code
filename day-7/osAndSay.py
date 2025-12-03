# let's work withe the  os module
import os
# get current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

os.mkdir('day-7/test_dir')
print("Directory 'test_dir' created.")
os.rmdir('day-7/test_dir')
print("Directory 'test_dir' removed.")
# create a new file
with open('day-7/test.txt', 'w') as file:
    file.write("This is a test file.")
print("File 'test.txt' created.")
# rename the file
os.rename('day-7/test.txt', 'day-7/renamed_test.txt')
print("File renamed to 'renamed_test.txt'.")
# delete the file
os.remove('day-7/renamed_test.txt')
print("File 'renamed_test.txt' deleted.")

os.remove('test.txt')
