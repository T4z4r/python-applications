#Palindrome: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.

def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')