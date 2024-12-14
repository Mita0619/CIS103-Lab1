class Array:
 def __init__(self, capacity, fill_value=None):
 self.items = [fill_value] * capacity

 def insert(self, index, value):
     self.items = self.items[:index] + [value] + self.items[index:]

 def delete(self, index):
     self.items = self.items[:index] + self.items[index + 1:]

def increase_size(self, new_capacity):
 self.items += [None] * (new_capacity - len(self.items))
def decrease_size(self, new_capacity):
 self.items = self.items[:new_capacity]

def __init__(self, data, next=None):
 self.data = data
 self.next = next

 class LinkedList:
     def __init__(self):
         self.head = None

     def insert_at_beginning(self, data):
         self.head = Node(data, self.head)

     def insert_at_end(self, data):
         if not self.head:
             self.head = Node(data)

     else:
     probe = self.head
     while probe.next:
         probe = probe.next
     probe.next = Node(data)

class LinkedList:
 def __init__(self):
 self.head = None
 def insert_at_beginning(self, data):
 self.head = Node(data, self.head)
 def insert_at_end(self, data):
 if not self.head:
 self.head = Node(data)
 else:
 probe = self.head
 while probe.next:
 probe = probe.next
 probe.next = Node(data)

 def delete_at_position(self, index):
     if index == 0:
         self.head = self.head.next
     else:
         probe = self.head
     for i in range(index - 1):
         probe = probe.next
     probe.next = probe.next.next if probe.next else None