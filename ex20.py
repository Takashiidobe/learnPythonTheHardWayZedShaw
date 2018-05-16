#the imports to use argv
from sys import argv

#sets the amount of argvs (script + the file to change)
script, input_file = argv

#defines the function print_all as reading the file
def print_all(f):
    print(f.read())

#defines rewinding the file as going back to the first line
def rewind(f):
    f.seek(0)

#defines printing a line as the line_count and readline
def print_a_line(line_count, f):
    print(line_count, f.readline())

#sets current file to be the file we've opened now
current_file = open(input_file)

print("First let's print the whole file: \n")

#print the whole file itself
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#sets the file back to the beginning.
rewind(current_file)

print("Let's print three lines:")

#sets the current line to be printed to the first line
current_line = 1

#prints the first line of the file
print_a_line(current_line, current_file)

#sets the current line to one more than it was previously then it prints it
current_line += 1
print_a_line(current_line, current_file)

#sets the current line to one more than it was previously then it prints it
current_line += 1
print_a_line(current_line, current_file)