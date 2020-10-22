from sys import argv
# get filename
script, filename = argv
# open a file
txt = open(filename) # run $ pydoc
# print file name and the file itself
print(f"Here's your file {filename}:")
print(txt.read())
# another input to print the file
print(f"Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# To run: $ ex15.py ex15_sample.txt