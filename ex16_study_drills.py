from sys import argv

script, filename = argv

print("Let's read the file.")

print("Opening the file...")
target = open(filename, 'r')

print("Printing the file content:")
print(target.read())

print("And finally, we close it.")
target.close()

# to run: $ python3 ex16_study_drills.py ex16_test.txt