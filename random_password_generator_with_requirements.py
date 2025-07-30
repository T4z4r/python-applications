import random
import string

def generate_password(length=12, requirements=None,include_special_chars = True, include_digits = True):
    characters = string.ascii_letters 
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    

password_length = int(input("Enter the desired password length (default is 12): ") or 12)
print("Generated Password:", generate_password(password_length))