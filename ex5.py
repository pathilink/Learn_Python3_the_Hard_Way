my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

print("----------------------------------------------------------")
# 1 lbs = 0.453592 kg
# 1 inch = 2.54 cm

name = 'Patrícia'
age = 35 # it's a lie
height = 63 * 2.54 # inches * centimeters
weight = round(132 * 0.453592, 2) # lbs * kg
eyes = 'brown'
teeth = 'white'
hair = 'black'

print(f"Let's talk about {name}.")
print(f"She's {height} centimeters tall.")
print(f"She's {weight} kilos heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {round(total, 2)}.")

