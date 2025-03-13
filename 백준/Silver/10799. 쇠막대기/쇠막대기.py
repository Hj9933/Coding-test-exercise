# 쇠막대기
lst = list(input())
A = []
tmp = 0
result = 0
for l in lst:
    if l == "(":
        A.append(l)
        tmp = l
    elif l == ')':
        if tmp == "(":
            A.pop()
            result += len(A)
        else:
            A.pop()
            result += 1
        tmp = l
print(result)