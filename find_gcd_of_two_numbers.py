def compute_gcd(x,y):
    while y:
        x,y=y,x%y
    return x

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("GCD:", compute_gcd(num1,num2))