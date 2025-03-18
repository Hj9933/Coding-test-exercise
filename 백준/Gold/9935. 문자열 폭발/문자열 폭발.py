# 폭발문자열
lst = list(input())
bombs = list(input())
stack = []
n = len(bombs)
for w in lst:
    stack.append(w)
    if stack[-n:] == bombs:
        for _ in range(n):
            stack.pop()

if stack:
    answer = ''.join(stack)
else:
    answer = 'FRULA'
print(answer)