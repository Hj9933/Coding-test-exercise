n = int(input())
command = [list(input().split()) for _ in range(n)]

class  Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.size() > 0:
            return self.data.pop()
        else:
            return -1
        
    def top(self):
        if self.size() > 0:
            return self.data[-1]
        else:
            return -1
        
stack = Stack()

for c in command:
    if c[0] == 'push':
        x = int(c[1])
        stack.push(x)
    elif c[0] == 'pop':
        print(stack.pop())
    elif c[0] == 'size':
        print(stack.size())
    elif c[0] == 'empty':
        print(stack.empty())
    else:
        print(stack.top())