n, k = map(int, input().split())

lst = list(range(1, n+1))
lst1 = ['<']
de = 0
while len(lst) != 0:
    de += k # k만큼 순번 증가
    de = de % len(lst)
    if de == 0: # de가 0이면 리스트의 마지막 숫자를 빼야하므로
        de = len(lst) - 1
    else:
        de = de - 1
    lst1.append(lst.pop(de))
lst1.append('>')

for i in range(n + 2):
    if i == 0 or i == 1 or i == n+1:
        print(lst1[i], end = '')
    else:
        print(',', lst1[i], end = '')