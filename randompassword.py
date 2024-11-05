import random
import string
password = ("")
special_chars = ("!", "@", "#", "$", "&", "*", "_", "-", ".", ",", ":", ";")
PasswordLengthComparer = 0
PasswordLength = int(input("What is the desired length of your password? >"))
while PasswordLengthComparer < PasswordLength:
	Character_Type = random.randrange(0,3)
	if Character_Type == 0:
		password += str(random.randint(0,9))
	elif Character_Type == 1:
		password += random.choice(string.ascii_letters)
	elif Character_Type == 2:
		password += random.choice(special_chars)
	PasswordLengthComparer += 1
print(password)
