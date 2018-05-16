
#imports from the system arguments
from sys import argv

#the script is always the first arg, and then the filename is the second
script, filename = argv

#simplifies the open(filename) command
txt = open(filename)

#a little line that says what we're doing
print(f"Here's your file {filename}:")
#prints out the contents of the file
print(txt.read())

#make sure to close files after you open them.
txt.close()

#asks for the filename again
print("Type the filename again:")
#saves whatever input you give it
file_again = input("> ")

#uses the input to open the file again
txt_again = open(file_again)
#opens the file
print(txt_again.read())

#always close files after you're done using them
txt.close()