import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = list(list(input()) for _ in range(n))

case1 = ['W','B','W','B','W','B','W','B']
case2 = ['B','W','B','W','B','W','B','W']

INF = int(1e9)
result = INF
for i in range(n-7):
    for j in range(m-7):
        # case1
        tmp = 0
        for k in range(i, i+8, 2):
            c = 0
            for l in range(j, j+8):
                if graph[k][l] != case1[c]:
                    tmp +=1
                if graph[k+1][l] != case2[c]:
                    tmp += 1
                c += 1
        result = min(result, tmp)
        # case2
        tmp = 0
        for k in range(i, i+8, 2):
            c = 0
            for l in range(j, j+8):
                if graph[k][l] != case2[c]:
                    tmp +=1
                if graph[k+1][l] != case1[c]:
                    tmp += 1
                c += 1            
        result = min(result, tmp)
            
print(result)