class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_find(head, target):
  node = head
  while node is not None:
    if node.val == target:
      return(True)
    node = node.next
  return(False)
