print("How old are you?", end=' ') # end=' ': this tells print to not end the line with a newline character and go to the next line
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")