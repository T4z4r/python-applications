def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")