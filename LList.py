class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class llist:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def iter(self):
        current = self.head
        while current:
            self.size += 1
            val = current.data
            print(current.data)
            current = current.next
            yield val
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    
    for i in range(len(array)):
        num = array[i]
        if outOfOrder(i,num,array):
            minOutOfOrder = min(minOutOfOrder,num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("-inf"):
        return [-1,-1]
        
    leftOutOfOrder = 0
    
    while minOutOfOrder >= array[leftOutOfOrder]:
        leftOutOfOrder+=1
    
    rightOutOfOrder = len(array)-1
    while maxOutOfOrder <= array[rightOutOfOrder]:
        rightOutOfOrder-=1
    
    return [leftOutOfOrder,rightOutOfOrder]
            

def outOfOrder(index,num, array):
    if index == 0:
        return num > array[index+1]
    if index == len(array)-1:
        return num < array[index-1]
    return num > array[index+1] or num < array[index-1]

print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))
    def removeNode(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                    self.size -= 1
            prev = current
            current = current.next

    def reverseList(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = self.head
        previous = None
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head = previous

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False


link = llist()

link.append(5)
link.append(6)
link.append(4)
link.reverseList()
link.iter()
print(link.search(6))
