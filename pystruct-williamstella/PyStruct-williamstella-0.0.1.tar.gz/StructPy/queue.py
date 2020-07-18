from node import Node
import logging

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)

      if self.is_empty():
        
        self.head = item_to_add
        self.tail = item_to_add
      
      else:
        
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      
      self.size += 1
    
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
      
      return item_to_remove.get_value()

    else:

      logger.error(" Cannot dequeue an empty Queue")

  def peek(self):
    if self.is_empty():
      
      logger.error(" Cannot peek on an empty Queue") 
    else:
      return self.head.get_value()
  
  def get_size(self):

    return self.size
  
  def has_space(self):

    if self.max_size == None:

      return True

    else:

      return self.max_size > self.get_size()
    
  def is_empty(self):

    return self.size == 0

