from collections import deque

t = int(input())
for _ in range(t):
    input_p = list(input())
    a = deque([])
    b = deque([])
    for w in input_p:
        if w == '<':
            if len(a) > 0:
                b.appendleft(a.pop())
        elif w == '>':
            if len(b) > 0:
                a.append(b.popleft())
        elif w == '-':
            if len(a) > 0:
                a.pop()
        else:
            a.append(w)
    a = ''.join(a)
    b = ''.join(b)
    ans = a+b
    print(ans)