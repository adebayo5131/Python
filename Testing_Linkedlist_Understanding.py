class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        lastNode = self.head

        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = new_node

    def deleteDuplicates(self):
        current = self.head
        while current is not None:
            if current.next and current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

    def printList(self):
        temp = self.head
        while (temp) is not None:
            print(temp.val)
            temp = temp.next


if __name__ == '__main__':
    linkNodes = LinkedList()

    linkNodes.push(1)
    linkNodes.append(2)
    linkNodes.append(2)
    linkNodes.append(2)
    linkNodes.append(3)
    linkNodes.append(3)
    linkNodes.append(4)
    linkNodes.append(4)
    linkNodes.append(5)
    linkNodes.push(6)

    linkNodes.printList()

    # Removing duplicates
    linkNodes.deleteDuplicates()
    print("\n Removing duplicates from Linked List")

    linkNodes.printList()
