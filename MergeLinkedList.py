# Add, edit, or remove tests in this file.
# Treat it as your playground!

import program
import unittest


class LinkedList(program.LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        list1 = LinkedList(1).addMany([2, 3, 4, 5])
        list2 = LinkedList(6).addMany([7, 8, 9, 10])
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_2(self):
        list1 = LinkedList(6).addMany([7, 8, 9, 10])
        list2 = LinkedList(1).addMany([2, 3, 4, 5])
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_3(self):
        list1 = LinkedList(1).addMany([3, 5, 7, 9])
        list2 = LinkedList(2).addMany([4, 6, 8, 10])
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_4(self):
        list1 = LinkedList(2).addMany([6, 7, 8])
        list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_5(self):
        list1 = LinkedList(1).addMany([2, 3, 4, 5, 7, 8, 9, 10])
        list2 = LinkedList(6)
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_6(self):
        list1 = LinkedList(6)
        list2 = LinkedList(1).addMany([2, 3, 4, 5, 7, 8, 9, 10])
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_7(self):
        list1 = LinkedList(1)
        list2 = LinkedList(2)
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_8(self):
        list1 = LinkedList(2)
        list2 = LinkedList(1)
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_9(self):
        list1 = LinkedList(1).addMany([1, 1, 3, 4, 5, 5, 5, 5, 10])
        list2 = LinkedList(1).addMany([1, 2, 2, 5, 6, 10, 10])
        output = program.mergeLinkedLists(list1, list2)
        expectedNodes = [1, 1, 1, 1, 1, 2, 2,
                         3, 4, 5, 5, 5, 5, 5, 6, 10, 10, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)


if __name__ == "__main__":
    unittest.main()
