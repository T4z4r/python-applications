import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) 

input_email = input("Enter an email address: ")
if is_valid_email(input_email):
    print(f"{input_email} is a valid email address.")
else:
    print(f"{input_email} is not a valid email address.")