import string
#pangram is a sentence that uses every letter of the alphabet at least once
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    s = s.lower()
    return alphabet.issubset(set(s))

input_string = input("Enter a string to check if it is a pangram: ")

if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")