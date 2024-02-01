import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst_1 = list(set(lst))
lst_1.sort()

# 처음에는 lst_1.index 사용해서 했으나 시간복잡도 이슈로 시간초과. index로 하면 최대 1000000번의 수행 이루어짐
# dictionary 써서 하면 해결
dic = {lst_1[i]: i for i in range(len(lst_1))} 

for i in lst:
    print(dic[i], end=' ')