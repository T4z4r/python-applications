def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
    
num=int(input("Enter a natural number: "))
print(f"The sum of the first {num} natural numbers is: {sum_of_natural_numbers(num)}")