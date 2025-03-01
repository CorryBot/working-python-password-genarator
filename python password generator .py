import random

def generate_password(pl):
	pw = ""
	pwc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
	for i in range(pl):
		pw += random.choice(pwc)
	return pw

pl = int(input("Enter the length of the password: "))
pw = generate_password(pl)
print(pw)
input("Press Enter to exit")