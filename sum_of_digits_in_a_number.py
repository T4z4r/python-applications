def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number = int(input("Enter a number: "))
print(f"The sum of the digits in {number} is: {sum_of_digits(number)}")