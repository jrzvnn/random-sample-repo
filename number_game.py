#Sample file for my git

# Number game
#  Rules: Guest the Random number given by the operator. The number is
# 0>number>=20.
import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
	guess = int(input("new nunmber:"))
	if guess > 0:
		if guess > to_be_guessed:
			print("Number too large")
		elif guess < to_be_guessed:
			print("Number too small")
	else:
		print("Sorry that you're giving up!")
else:
	print("Congratulations, You made it!")
