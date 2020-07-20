class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.linked_node = linked_node
    
  def set_next_node(self, linked_node):
    self.linked_node = linked_node

  def __repr__(self):
    return self.value
 
  def get_next_node(self):
    return self.linked_node
  
  def get_value(self):
    return self.value
