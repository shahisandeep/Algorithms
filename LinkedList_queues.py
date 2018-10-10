class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Linked_list:

    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp is not None:
            print temp.head
            temp  = temp.next

l = Linked_list()

n1 = Node(20)
n2 = Node(40)
n3 = Node(50)

l.head = n1
n1.next = n2
n2.next = n3
print l.traverse()




