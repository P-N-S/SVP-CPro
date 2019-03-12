# Count pairs in array whose sum is divisible by K
# https://www.geeksforgeeks.org/count-pairs-in-array-whose-sum-is-divisible-by-k/
# SGVP 394500 | 15:27 12Mar19
# Given an array A[] and positive integer K, count total number of pairs in the array
# whose sum is divisible by K.

# IN : A[] = {2, 2, 1, 7, 5, 3}, K = 4
# OP : 5

# There are five pairs possible whose sum is divisible by '4' i.e, (2, 2),
# (1, 7), (7, 5), (1, 3) and (5, 3)

def countKdivPairs(A, n, K):

    # Create a frequency array to count occurrences of all remainders when 
    # divide by K

    freq = [0] * K

    # Countr occurrences of all remainders
    for i in range(n):
        freq[A[i] % K]+= 1

    sum = freq[0] * (freq[0] - 1) / 2;

    # count for all i and (K - i) )
    i = 1
    while( i <= K//2 and i != (K - i) ):
        sum += freq[i] * freq[K-i]
        i+= 1


    # If K is even
    if ( K % 2 == 0 ):
        sum += (freq[K//2] * (freq[K//2]-1)/2);

    return int(sum)


# Drvier code
A = [2, 2, 1, 7, 5, 3]
n = len(A)
K = 4
print(countKdivPairs(A, n, K))
