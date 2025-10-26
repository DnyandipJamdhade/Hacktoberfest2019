# password_generator.py
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Enter password length: "))
print("Generated password:", generate_password(length))
