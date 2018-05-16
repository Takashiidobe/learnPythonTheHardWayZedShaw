#close (closes the file)
#read (reads the file)
#readline(reads just one line of a text file
#truncate (empties the contents of the file)
#write('stuff') Writes stuff to the file
#seek(0) moves the read/write location to the beginning of the file


#again the importing argv
from sys import argv


#these are the vars that we'll be assigning to argv
script, filename = argv

#This is the prompt that says CTRL-C to cancel, or return to continue
print(f"We're going to erase {filename}.")
print("if you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

#sets the input to a question mark instead of a blank mark in the terminal
input("?")

#prints out a line telling us that it's working
print("Opening the file...")
#sets the open filename to a var (target)
#w opens the file for writing, while truncating the file first
target = open(filename, 'w')

#prints out a warning that it's clearing the file
print("Truncating the file. Goodbye!")
#clears out the file itself
target.truncate()

#asks for three lines
print("Now I'm going to ask you for three lines.")
#saves the three lines given to three vars
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#gives us more instruction that we're going to overwrite the file with this
print("I'm going to write these to the file.")

#prints out the three lines while indenting
target.write(f"{line1} \n {line2} \n {line3} \n")

#closes the file
print("And finally, we close it.")
#closes the file in an action
target.close()