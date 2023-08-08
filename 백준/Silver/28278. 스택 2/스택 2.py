class stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def size(self):
        return len(self.data)
    def isEmpty(self):
        if self.size() == 0:
            return 1
        else: 
            return 0
    def pop(self):
        if self.isEmpty() == 0:
            return self.data.pop()
        else:
            return -1
    def peek(self):
        if self.isEmpty() == 0:
            return self.data[-1]
        else:
            return -1

import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

stack = stack()
for i in range(n):
    if lst[i][0] == 1:
        stack.push(lst[i][1])
    elif lst[i][0] == 2:
        print(stack.pop())
    elif lst[i][0] == 3:
        print(stack.size())
    elif lst[i][0] == 4:
        print(stack.isEmpty())
    else:
        print(stack.peek())