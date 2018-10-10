class Queue:
    def __init__(self):
        self.queue = []

    def push(self, data):
        return self.queue.insert(0,data)

    def peek(self):
        return self.queue[-1]

    def pop(self):
        return self.queue.pop()

    def traverse(self):
        return self.queue
if __name__ == '__main__':
    q = Queue()
    q.push(20)
    q.push(40)

    print q.traverse()