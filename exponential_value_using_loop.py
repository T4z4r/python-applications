base=int(input("Enter the base of the exponential function: "))
exponent=int(input("Enter the exponent of the exponential function: "))
result = 1

for _ in range(exponent):
    result *= base
    
print(f"The result of {base} raised to the power of {exponent} is: {result}")