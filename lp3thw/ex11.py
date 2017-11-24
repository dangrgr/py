print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f'So, your {age} years old, {height} tall and {weight} lbs.')


print("Ok, lets do a little math: ")
x = int(input("How old is your wife? "))
if x < int(age):
	print("Your wife is yonger than you!")
elif x > int(age):
	print("Your wife is older than you!")
else:
	print("You and your wife are the same age!")