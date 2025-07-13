def count_vowels(string):
    vowels= "aeiouAEIOU"
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string to count vowels: ")
print(f"The number of vowels in '{string}' is: {count_vowels(string)}")