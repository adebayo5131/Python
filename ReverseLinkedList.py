#O(n) time and O(1) space where n is the number of nodes in the linkedlist
def reverseLinkedList(head):
	current1 = None
	current2 = head
	while current2:
		current3 = current2.next
		current2.next = current1
		
		current1 = current2
		current2 = current3
	return current1
		