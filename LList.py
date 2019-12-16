
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class llist:
    def __init__(self):
        self.head = None

    def append(self,new_val):

        new_node = Node(new_val)

        if self.head is None:
            self.head = new_node

        current = self.head
        while self.head:
           current.next = new_node

    def print(self):

        while self.head:
            print(self.head.next)


ll = llist()

ll.append(5)
ll.append(6)
ll.append(4)
ll.print()

