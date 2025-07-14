#Anagram: a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

def is_anagram(s1, s2):
   return sorted(s1) == sorted(s2)

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")