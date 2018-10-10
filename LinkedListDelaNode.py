class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while node is not None:
            print node.data
            node = node.next




l = LinkedList()
n2 = Node(30)
n3 = Node(40)
l.head = Node(20)

l.head.next = n2
n2.next = n3







l.traverse()



