# https://www.geeksforgeeks.org/python-program-to-check-if-given-string-is-pangram/
# Python program to check if given string is pangram
# A pangram is a sentence containing every letter in the Enlish Alphabet

import string

def isPangram_Naive(str):
    print("isPangram_Naive() - start | 17:15 19F19")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

        
    return True

    # Driver code
    string = 'The quick brown fox jumps over the lazy dog'
    if(isPangram_Naive(string) == True):
        print("Yes, it's pangram")
    else:
        print("No, it's not pangram")