# https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/
# Array in Python | Set1(introduction and functions)
# SGVP384750 | 13:48 19F19

# Python code to demo the working of array(), append(), insert()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print ("The new created array is : ", end=" ")
for i in range (0, 3):
    print(arr[i], end=" ")

print("\r")

# using append() to insert new value at end
arr.append(4)

# printing appended array
print("The appended array is : ", end="")
for i in range (0, 4):
    print (arr[i], end=" ")

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)

print("\r")

# printing array after insertion
print("The array after insertion is: ", end="")
for i in range (0, 5):
    print (arr[i], end=" ")


# using pop() to remove element at 2nd position
# SGVP385400 | 20F19

print("The popped element is : ", end=" ")
print(arr.pop(2));


#using remove() to remove 1st occurrence of 1
arr.remove(1)

print("The array after removing is :", end="")
for i in range(0, len(arr)):
    print(arr[i], end=" ")