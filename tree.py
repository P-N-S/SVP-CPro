# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# SGVP384750 | 20:47 19F19

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):

    #print("printInorder() - start | 20:49 19F19")
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)

# A function to do postorder tree traversal
def printPostorder(root):
    #print("printPostoder() | 20:02 10F19")

    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),


# Driver Code
print("Driver Code | 20:04 20F19")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Inorder traversal of binary tree is")
printInorder(root)

print("Postorder traversal of binary tree is")
printPostorder(root)