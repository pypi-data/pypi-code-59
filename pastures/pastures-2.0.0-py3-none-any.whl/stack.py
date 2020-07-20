import logging

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  def __repr__(self):
    return self.value
    
  def set_next_node(self, link_node):
    self.link_node = link_node
    
  def get_next_node(self):
    return self.link_node

  def delete_next_node(self):
    self.link_node = None
  
  def get_value(self):
    return self.value

class Stack:
  def __init__(self):
    self.node_list = []
    self.length = 0
    self.most_recent_node = None
 
  def __str__(self):
    return str(self.node_list)

  def push(self, value):
    new_node = Node(value)
    new_node.set_next_node(self.most_recent_node)
    self.length += 1
    self.node_list.append(new_node)

  def pop(self):
    if not self.is_empty():
      
      self.length -= 1 
      return self.node_list.pop()

    logging.error(" Cannot pop from an empty Stack")    

  def peek(self):
    if not self.is_empty():

      return self.node_list[-1]

    logging.error(" This Stack is empty")

  def has_space(self):
    if self.limit == None:
      return True

    else:
      return self.limit > self.size

  def is_empty(self):

    return self.length == 0
  

x = Stack()
x.push("1")
x.push("2")
print(x)
x.pop()
print(x)
x.peek()
print(x)
