def find_median(a,b,c):
    return sorted([a, b, c])[1]

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print(f"The median of {num1}, {num2}, and {num3} is: {find_median(num1, num2, num3)}")