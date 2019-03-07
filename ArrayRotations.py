#Array Rotations | SGVP386100 | 21F19
#https://www.geeksforgeeks.org/array-data-structure/#rotation
#https://www.geeksforgeeks.org/array-rotation/

# Program for Array Rotation

# Method 2 (Rotate one by one)
def leftRotate(arr, d, n):
    print("leftRotate() | 15:21 21F19")
    for i in range(d):
        leftRotatebyOne(arr, n)

# Function to left Rotate arr[] of size n by 1
def leftRotatebyOne(arr, n):
    print("leftRotatebyOne() | 15:23 21F19")
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp


# Method 3 - A Juggling Algorithm
# Function to left rotate arr[] of size n by d
def leftRotate_JugglingAlgorithm(arr, d, n):
        for i in range(gcd(d, n)):
                # move i-th values of blocks
                temp = arr[i]
                j = i
                while 1:
                        k = j + d
                        if k >= n:
                                k = k - n
                        if k == i:
                                break
                        arr[i] = arr[k]
                        j = k
                arr[j] = temp


# gcd
def gcd(a, b):
        if b == 0:
                return a
        else:
                return gcd(b, a%b)
                


# utility fun to print an array
def printArray(arr, size):
    print("printArray() | 15:25 21F19")
    for i in range(size):
        print("%d"% arr[i], end=" ")


# Driver prog
arr = [1, 2, 3, 4, 5, 6, 7]
#leftRotate(arr, 2, 7)
leftRotate_JugglingAlgorithm(arr, 2, 7)
printArray(arr, 7)
