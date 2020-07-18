from node import Node
import logging

class Stack:
  def __init__(self, limit=None):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():

      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1

    else:

      logging.error(" Pushing this Node will exceed the limit for this Stack")

  def pop(self):
    if not self.is_empty():

      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()

    logging.error(" Cannot pop from an empty Stack")    

  def peek(self):
    if not self.is_empty():

      return self.top_item.get_value()

    logging.error(" This Stack is empty")

  def has_space(self):
    if self.limit == None:

      return True

    else:

      return self.limit > self.size

  def is_empty(self):

    return self.size == 0
  
