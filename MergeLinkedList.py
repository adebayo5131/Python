class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    tempNode = LinkedList(0)
    temp = tempNode
    while headOne is not None and headTwo is not None:
        if headOne.value < headTwo.value:
            temp.next = headOne
            headOne = headOne.next
        else:
            temp.next = headTwo
            headTwo = headTwo.next
        temp = temp.next

    if headOne is None:
        temp.next = headTwo
    else:
        temp.next = headTwo
    return tempNode.next
