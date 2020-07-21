class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        def printTree(self):
            if self.left:
                self.left.printTree()
            print(self.data),
            if self.right:
                self.right.printTree()
        def insert(self, data):

            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data
        def findval(self, lkpval):
            if lkpval < self.data:
                if self.left is None:
                    return str(lkpval)+" Not Found"
                return self.left.findval(lkpval)
            elif lkpval > self.data:
                if self.right is None:
                    return str(lkpval)+" Not Found"
                return self.right.findval(lkpval)
            else:
                print(str(self.data) + ' is found')

class binary_tree:
    def __init__(self, values):
        self.tree = None
        if values:
            head = Node(values[0])
            for value in values:
                head.insert(value)
        self.tree = head
        print(self.tree)
   
        
    
                     
                        
            

