""" Python program to merge two
sorted linked lists """


# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode


# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def mergeLists(listA, listB):
    prehead = Node(-1)
    prev = prehead
    while True:
        if listA is None:
            prev.next = listB
            break
        if listB is None:
            prev.next = listA
            break

        if listA.data <= listB.data:
            prev.next = listA
            listA = listA.next
        else:
            prev.next = listB
            listB = listB.next
        
        prev =prev.next

    return prehead.next

# Create 2 lists
listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
listA.addToList(1)
listA.addToList(4)
listA.addToList(5)

listB.addToList(1)
listB.addToList(2)
listB.addToList(3)
listB.addToList(6)

# Call the merge function
listA.head = mergeLists(listA.head, listB.head)

# Display merged list
print("Merged Linked List is:")
listA.printList()
