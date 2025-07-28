def print_factors(n):
    factors=[]
    for i in range(1,n+1):
        if n%1==0:
            factors.append(i)
    return factors

number=int(input("Enter a number to find its factors:"))
print("Factors of",number,"are:",print_factors(number))