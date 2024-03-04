n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))
    
tri_sum = tri.copy()
if n == 1:
    print(tri[0][0])
else:
    tri_sum[1] = [(tri_sum[0][0] + i) for i in tri[1]]

    for i in range(2, n):
        tri_sum[i][0] = tri_sum[i-1][0] + tri_sum[i][0] # 해당 층의 처음과 끝은 길이 하나
        tri_sum[i][-1] = tri_sum[i-1][-1] + tri_sum[i][-1]
        for j in range(1, len(tri[i])-1):
            tri_sum[i][j] = max(tri_sum[i-1][j-1], tri_sum[i-1][j]) + tri[i][j]
    print(max(tri_sum[n-1]))