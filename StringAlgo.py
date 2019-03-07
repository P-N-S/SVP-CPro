# https://www.geeksforgeeks.org/python-program-to-check-if-given-string-is-pangram/
# Python program to check if given string is pangram
# A pangram is a sentence containing every letter in the Enlish Alphabet

import string

# Approach 1
def isPangram_Naive(str):
    print("isPangram_Naive() - start | 17:15 19F19")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

        
    return True

# Approach 2 : Using Python Set
# Convert the given string into set and then check if the alphabet set is greater
# than or equal to it or not. If the string set is greater or equal, print 'Yes'
# otherwise 'No'.
alphabets = set(string.ascii_lowercase)

def isPangram_Set(string):
    print("isPangram_Set() - Start | 17:27 19F19")
    return set(string.lower()) >= alphabets

# Driver code
print("ONS! Driver Code - Start | 17:18 19F19")
string = 'The quick brown fox jumps over the lazy dog'
if(isPangram_Naive(string) == True):
    print("Yes, it's pangram")
else:
    print("No, it's not pangram")

if(isPangram_Set(string) == True):
    print("Yes")
else:
    print("No")