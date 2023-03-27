def insert_at_end(self, data):
 newNode = Node(data)
 if self.head is None:
 self.head = newNode
 self.tail = newNode
 else:
 self.tail.next = newNode
 self.tail = newNode
 self.length+=1
 return self
