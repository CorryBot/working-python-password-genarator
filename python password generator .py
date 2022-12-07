import random

num=2

while num>0:
   def generate_password():
     password_length = 15 # Set the       length of the password here

  # Create a string of all the possible characters that can go into the password
     password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"

  # Initialize the password as an empty string
     password = ""

  # Choose random characters and add them to the password until it reaches the desired length
     for i in range(password_length):
       password += random.   choice(password_characters)

     return password

# Generate a password and print it to the screen
   print(generate_password())
   num=num-1