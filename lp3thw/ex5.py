name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Lets talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# 2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. 
# Do not just type in the measurements. Work out the math in Python.


cm_in_inch = 2.54
inch_in_cm = 0.393701
cm = 100
inches = 12
cm_calc = inches * cm_in_inch
in_calc = cm * inch_in_cm
print(f"There are {cm_calc} centemeters in {inches} inches.")
print(f"There are {in_calc} inches in {cm} centemeters.")