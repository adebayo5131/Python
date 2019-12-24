class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Using preorder traversal this will produce a sorted L-R order
    #Using preorder traversal this will produce a sorted L-R order
	#(O(V+E) time, vertexs plus edges and space is O(v)
    def depthFirstSearch(self, array):
        if self is None:
            return None
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


test4 = Node("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")
array = []
print(test4.depthFirstSearch(array), "\n")
