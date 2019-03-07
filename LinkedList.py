# https://www.geeksforgeeks.org/linked-list-set-1-introduction/
# Linked List | Set 1 (Introduction)
# 18F19

#Node class
class Node:

    print("Node class")
    # Function to initialize the Node object
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked List class
class LinkedList:
    
    print("LinkedList Class")
    # Function to initialize the LinkedList object
    def __init__(self):
        self.head = None

    # This function prints contents of linked list starting from head
    def printList(self):
        print("printList() - start | 19:25 19F19")
        temp = self.head
        while (temp):
            print (temp.data),
            temp = temp.next

# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
# SGVP384750 | 19F19

    def push(self, new_data):
        print("push() - start | 19:24 19F19 ",+new_data)
        new_node = Node(new_data)
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        print("insertAfter() - Start | 19:25 19F19", new_data)
        if prev_node is None:
            print ("The given previous node must in LinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
# SGVP385500|20F19
    def append(self, new_data):
        print("append() - Start | 19:31 20F19")
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #   new node as head
        if self.head is None:
            self.head = new_node
            return
        
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    #https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
    # SGVP388500 | 17:47 28F19
    def deleteNode(self, key):
        print("deleteNode() - Start | 18:47 28F19")
        temp = self.head
        if (temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            #temp = temp.next
        
        if (temp == None) :
            return
        
        prev.next = temp.next
        temp = None


# Code execution starts here
if __name__ == '__main__':

    print("__main__ start | 17:54 18F19")
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third  = Node(3)

    llist.head.next = second

    second.next = third

    llist.printList()

    #push
    llist.push(0)
    llist.push(7)

    #insertAfter
    llist.insertAfter(llist.head.next, 9)
    llist.printList()

    #append
    llist.append(3)
    llist.append(4)         
    llist.printList()

    #delete node | 18:47 28F19
    llist.deleteNode(3)
    print("List after deletion")
    llist.printList()   