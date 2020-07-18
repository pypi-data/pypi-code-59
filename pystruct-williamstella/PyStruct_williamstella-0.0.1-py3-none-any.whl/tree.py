class TreeNode:

  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    
    self.children.append(child_node)
    
  def remove_child(self, child_node):

    self.children = [child for child in self.children 
                     if child is not child_node]
    
  def traverse(self):
    return self.value
    for node in self.children:
      return node.value
