class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        def printTree(self, layer = 0, orientation ="root"):
            u = layer+1
            print(f"{orientation} => {layer}:  {self.data}")
            if self.left:
                self.left.printTree(u, orientation="left")
            
              
            if self.right:
                self.right.printTree(u,orientation="right")
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
        def remove(self, value, parentNode = None):
            currentNode = self
            while currentNode is not None:
                if value<currentNode.data:
                    parentNode = currentNode
                    currentNode =currentNode.left
                elif value >currentNode.data:
                    parentNode =currentNode
                    currentNode =currentNode.right
                else:
                    if currentNode.left is not None and currentNode.right is not None:
                        currentNode.data = currentNode.right.getMinValue()
                        currentNode.right.remove(currentNode.data, currentNode)
                    elif parentNode is None:
                        if currentNode.left is not None:
                            currentNode.data =currentNode.left.data
                            currentNode.right = currentNode.left.right
                            currentNode.left = currentNode.left.left
                        elif currentNode.right is not None:
                            currentNode.data = currentNode.right.data
                            currentNode.left = currentNode.right.left
                            currentNode.right = currentNode.right.right
                        else:
                            pass

                    elif parentNode.left ==currentNode:
                        parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                    elif parentNode.right == currentNode:
                        parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                    break
            return self
        def getMinValue(self):
            currentNode = self
            while currentNode.left is not None:
                currentNode = currentNode.left
            return currentNode.data
                
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
    def printTree(self):
        self.tree.printTree()
        
   
        
    
                     
                        
            

