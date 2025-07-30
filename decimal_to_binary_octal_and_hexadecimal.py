dec=int(input("Enter a decimal number: "))

print(f"Binary: {bin(dec)[2:]}")
print(f"Octal: {oct(dec)[2:]}")
print(f"Hexadecimal: {hex(dec)[2:].upper()}")