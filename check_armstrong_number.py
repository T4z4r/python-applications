# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
# For example, 153 is an Armstrong number because 1³ + 5³ + 3³ = 1 + 125 + 27 = 153. 

def is_armstrong(n):
    order = len(str(n))
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return n == sum

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")