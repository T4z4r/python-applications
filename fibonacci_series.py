def fibonacci_series(n):
    a,b=0,1
    for _ in range(n):
        print(a, end="")
        a,b=b,a+b
        
terms=int(input("Enter the number of terms: "))
print("Fibonacci series.")
fibonacci_series(terms)