def remove_at_end(self):
    if self.head is None:
      print("Linked list is empty")
       return
 temp = self.head
 pre = self.head
 while temp.next:
  pre=temp
  temp=temp.next
  self.tail = pre
   self.tail.next = None
   self.length-=1
 if self.length == 0:
    self.head = None
    self.tail = None
    return temp
