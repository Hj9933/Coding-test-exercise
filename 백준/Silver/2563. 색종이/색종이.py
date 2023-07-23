paper = [[0]*100 for i in range(100)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i-1][b+j-1] = 1

r = 0
for i in paper:
    r += sum(i)

print(r)
