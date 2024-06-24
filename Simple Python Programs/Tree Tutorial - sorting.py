# Tree Tutorial : sorting
class Node():
    # method runs when the object is defined 
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # method to insert data to Tree
    def insert(self, data):
        if data < self.data :
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data :
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
    # Method to print Tree data in ascending order
    def printTree(self):
        if self.left:
            self.left.printTree()  # pointer moved to left most 
        print(self.data)  #print left most node value or the right most value
        if self.right:
            self.right.printTree() 
        return    
            
    
root = Node(10)
root.insert(5)
root.insert(6)
root.insert(1)
root.insert(4)
root.insert(2)
root.insert(9)
root.insert(12)
root.insert(15)
root.insert(11)
root.printTree()