# Find the element that appears once
# https://www.geeksforgeeks.org/find-the-element-that-appears-once/
# SGVP387500 | 14:47 26F19

# fun to find the element that appears once
def getSingle(arr, n):
    print("getSingle()- start | 14:55 26F19")
    ones = 0
    twos = 0

    for i in range(n):
        twos = twos | (ones & arr[i])
        ones = ones ^ arr[i]

        common_bit_mask = ~(ones & twos)

        ones &= common_bit_mask

        twos &= common_bit_mask

    return ones

# Detect if two integers have opposite signs
# https://www.geeksforgeeks.org/detect-if-two-integers-have-opposite-signs/
# SGVP 388500 | 13:28 28F19

def oppositeSigns(x, y):
    print("oppositeSigns() - Start | 13:31 28F19")
    return ((x ^ y) < 0)

# driver code

#element that appears once
print("The Driver Code | 14:55 26F19")
arr = [3, 3, 2, 3]
n = len(arr)

print("The element with single occurrence is ", getSingle(arr, n))
# end 

# Opposite sign

x = 100
y = 1
if (oppositeSigns(x, y) == True):
    print("Signs are opposite")
else:
    print("Signs are not opposite")