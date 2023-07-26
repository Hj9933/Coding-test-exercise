import sys
input = sys.stdin.readline
k = int(input())

class Stack:
    def __init__(self):
        self.data = []
    def size(self):
        print(len(self.data))
    def push(self, item):
        self.data.append(item)
    def pop(self):
        self.data.pop()

stack = Stack()

for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.push(n)
        
print(sum(stack.data))