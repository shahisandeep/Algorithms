# Valid Parenthesis using stack
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return 0 == self.size()

class Solution(object):


    def isValid(self, exp):
        s = Stack()
        opn = ['(', '{', '[']
        close = [')', '}', ']']
        for item in range(len(exp)):
            if exp[item] in opn:
                s.push(exp[item])
            if exp[item] in close:
                if s.is_empty():
                    return False
                    break
                else:
                    s.pop()

        return s.is_empty()

if __name__ == '__main__':

    valid = Solution()
    print valid.isValid(exp= '(])')











