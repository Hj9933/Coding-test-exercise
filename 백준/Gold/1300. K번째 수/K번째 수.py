# 1300 K번째 수
n = int(input())
k = int(input())


s, e = 1, n*n

while s <= e:
    temp = 0
    mid = (s+e)//2
    for i in range(1, n+1):
        temp += min(mid//i, n)

    if temp < k:
        s = mid + 1
    elif temp >= k:
        answer = mid
        e = mid - 1
print(answer)