class binary_tree:
    def __init__(self):
        print('this is a binary tree')
        
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        def print_tree(self):
            print(self.value)
        def insert(self, value)
            if self.value:
                if value < self.value:
                    if self.left is None:
                        self.left = Node(value)
                    else:
                        self.left.insert(value)
                elif value >self.value:
                    if self.right is None:
                        self.right =Node(value)
                    else:
                        self.right.insert(value)
            else:
                self.value = value
                     
                        
            
if __name__ == '__main__':
    binary_tree()
