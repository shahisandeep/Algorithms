class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = node(value)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node

    def insertAfterKthNode(self, prev_node, new_val):

        new_node = node(new_val)
        temp = self.head

        while temp.next is not None:
            if temp.data == prev_node:
                print "Node found"
                found = temp
                nextNode = temp.next
                new_node.next = nextNode
                found.next = new_node
                break
            temp = temp.next

    def traverseKthtoEnd(self,k):

        temp = self.head
        while temp.next is not None:
            if temp.data is k:
                print k, "found"
                temp = self.head





    def traverse(self):
        temp = self.head
        while temp is not None:
            print temp.data
            temp = temp.next

if __name__ == '__main__':
    l = Linked_list()
    l.head = node(80)

    l.append(90)
    l.append(100)
    l.append(200)
    l.append(400)
    l.insert(70)

    l.insertAfterKthNode(prev_node = 100, new_val = 240)
    l.traverse()

    print "traverse after kth Node"
    l.traverseKthtoEnd(90)
