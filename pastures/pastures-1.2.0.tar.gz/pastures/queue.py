import logging

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
  
  def __repr__(self):
    return str(self.value)
  
  def set_next_node(self, link_node):
    self.link_node = link_node
    
  def get_next_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    self.node_list = []

  def __repr__(self):
    return str(self.node_list)
 
  def enqueue(self, value):
    if self.is_full() == False:
      item_to_add = Node(value)

      if self.is_empty():
        
        self.head = item_to_add
        self.tail = item_to_add
      
      else:
        
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      
      self.size += 1
      self.node_list.append(item_to_add)
    
    else:
        logging.error(" Enqueueing a Node will exceed the maximum size")
         
  def dequeue(self):
    if self.get_size() > 0:

      item_to_remove = self.head

      if self.get_size() == 1:
        
        self.head = None
        self.tail = None

      else:
        
        self.head = self.head.get_next_node()
      
      self.size -= 1
      
      return self.node_list.pop(0)
    else:

      logger.error(" Cannot dequeue an empty Queue")

  def peek(self):
    if self.is_empty():
      
      logger.error(" Cannot peek on an empty Queue") 
    else:
      return self.head.get_value()
  
  def get_size(self):

    return self.size
  
  def is_full(self):

    if self.max_size == None:

      return True

    else:

      return self.max_size > self.get_size()
    
  def is_empty(self):

    return self.size == 0



