def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", add(num1, num2))
print("Difference:", subtract(num1, num2))
print("Product:", multiply(num1, num2))
print("Quotient:", divide(num1, num2))