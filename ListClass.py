# Python List | SGVP386100 | 18:00 21F19

# https://www.geeksforgeeks.org/python-list/

List = []
print("Initial blank List: ")
print(List)

# Creating a List with the use of a String
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)

# 18:51 26F19
# Creating a List with the use of mulitple values
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])

#Creating a Multi-Dimensional List
#(By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

# Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Intial blank List: ")
print(List)

# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)