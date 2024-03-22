n, m = map(int, input().split())
notlisten = set()
notsee = set()

for _ in range(n):
    notlisten.add(input())
for _ in range(m):
    notsee.add(input())

inter = notlisten.intersection(notsee)
inter = sorted(list(inter))
print(len(inter), *inter, end = '\n')