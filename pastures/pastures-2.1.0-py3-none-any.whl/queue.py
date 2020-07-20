import logging

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
  
  def __repr__(self):
    return str(self.value)
  
class Queue:
  def __init__(self, max_size=None):
    self.size = 0
    self.node_list = []

  def __repr__(self):
    return str(self.node_list)
 
  def enqueue(self, value):
    item_to_add = Node(value)

    self.size += 1

    self.node_list.insert(0, item_to_add.value)
    
  def dequeue(self):
    if self.get_size() > 0:
      self.size -= 1
      
      self.node_list.pop()
    else:

      logger.error(" Cannot dequeue an empty Queue")

  def peek(self):
    if self.is_empty():
      
      logger.error(" Cannot peek on an empty Queue") 
    else:
      return self.node_list[-1]
  
  def get_size(self):

    return self.size
    
  def is_empty(self):

    return self.size == 0

