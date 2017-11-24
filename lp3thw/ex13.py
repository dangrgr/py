from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

text = input("What was one of the 3 parameters you entered?" )
match = False

for item in argv:
    if item == text:
        match = item

if match:
    print(f"You told the truth! {text} was indeed one of the parameters you entered.")
else:
    print(f"Liar! {text} was NOT one of the parameters you entered!")

