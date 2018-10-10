import sys
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, nodee):
        if val < nodee.data:
            if nodee.left is None:
                nodee.left = Node(val)
            else:
                self._add(val, nodee.left)
        else:
            if val > nodee.data:
                if nodee.right is None:
                    nodee.right = Node(val)
                else:
                    self._add(val, nodee.right)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, nodee):
        if nodee is not None:
            self._printTree(nodee.left)
            print (str(nodee.data))
            self._printTree(nodee.right)

    def find(self, val):
        if self.root is not None:
            self._find(val, self.root)
        else:
            return None

    def _find(self, val, nodee):
        if val == nodee.data:
            print nodee.data
        elif val < nodee.data and nodee.left is not None:
            self._find(val, nodee.left)
        elif val > nodee.data and nodee.left is not None:
            self._find(val, nodee.right)

    def val(self):
        return self.validBST(self.root, min = - sys.maxint , max = sys.maxint)

    def validBST(self, node , min , max):
        if self.root is None:
            return True
        if min < node.data < max:
            if node.left is not None:
                self.validBST(node.left, min, node.data)
            if node.right is not None:
                self.validBST(node.right,  node.data ,max)
        return True

# Use the insert method to add nodes
if __name__ == '__main__':


    T = Tree() 
    T.add(20)
    T.add(9)
    T.add(21)
    T.add(8)
    T.add(10)
    T.add(22)
    T.printTree()
    print "Finding node"
    T.find(8)
    T.find(10)
    print T.val()
