import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def val(self, root):
        return self.validBST(root, min = - sys.maxint , max = sys.maxint)

    def validBST(self, node , min , max):

        if node.data is None:
            return True
        if min < node.data < max:
            if node.left is not None:
                self.validBST(node.left, min, node.data)
            if node.right is not None:
                self.validBST(node.right,  node.data ,max)
                print "Binary Search Tree"
        else:
             print ("Not a binary ST")
root = Node(20)
left_child = Node(18)
right_child = Node(22)

root.left = left_child
root.right = right_child

root.val(root)





