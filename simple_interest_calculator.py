# Prompt the user to enter the principal amount and convert it to float
p = float(input("Enter the principal amount: "))

# Prompt the user to enter the rate of interest and convert it to float
r = float(input("Enter the rate of interest: "))

# Prompt the user to enter the time in years and convert it to float
t = float(input("Enter the time in years: "))

# Calculate simple interest using the formula: (principal * rate * time) / 100
interest = (p * r * t) / 100

# Display the calculated simple interest
print(f"The simple interest is: {interest}")