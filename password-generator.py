import string
import random

alphabet = string.ascii_letters

numbers = string.digits

symbols = string.punctuation

length = int(input("Please enter your password length: "))

f = alphabet + numbers + symbols

password = "".join(random.sample(f, length))

print(password)





