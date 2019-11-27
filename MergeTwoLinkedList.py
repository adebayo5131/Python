# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        tempNode = ListNode(0)
        temp =   tempNode

        while (l1 != None and  l2!=None):
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            
        if l1 is None:
            temp.next = l2
        else:
            temp.next = l1
        return tempNode.next
     



