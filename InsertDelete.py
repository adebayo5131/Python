import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomized = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.randomized:
            self.randomized.add(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomized:
            self.randomized.remove(val)
            return True
        else:
            return False

    # def getRandom(self):
    #     indx = random.randint(0, 3)
    #     return list(self.randomized)[indx]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(5))
print(obj.insert(6))
print(obj.insert(7))
print(obj.insert(1))
print(obj.insert(5))
print(obj.remove(2))
print(obj.remove(7))
# print(obj.getRandom())
