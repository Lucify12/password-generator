import string
import random

alphabet = string.ascii_letters

numbers = string.digits

symbols = string.punctuation

length = int(input("Please enter your password length: "))

random_password = alphabet + numbers + symbols

password = "".join(random.sample(random_password, length))

print(password)
