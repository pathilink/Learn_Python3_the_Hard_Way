from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_line = open(from_file)
indata = in_line.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_line.close()

'''
to run:

first make a simple file:
$ echo "This is a test file." > test.txt

then look at it
$ cat test.txt
This is a test file.

now run the script
$ python3 ex17.py test.txt ex17_new_file.txt
'''