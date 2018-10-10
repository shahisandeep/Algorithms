class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        return self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        if len(self.stack) is None:
            return True
        else:
           return False


if __name__ == '__main__':
    s = Stack()
    s.push(20)
    s.push(50)
    s.push(80)

    s.peek()
    print s.pop()
    print s.pop()