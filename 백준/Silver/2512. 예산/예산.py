n = int(input())
req = list(map(int, input().split()))
m = int(input())

start = 1
end = max(req)
result = []
if sum(req) <= m:
    answer = end
else:
    while start <= end:
        mid = (start + end)//2
        # print(mid)
        s = 0
        for r in req:
            s += min(mid, r)
        # if s == m:
        #     answer = end
        #     break
        if s <= m: # 합이 총 예산보다 작으면 합을 늘려야하므로 start를 mid+1
            start = mid + 1
            answer = mid
        else: # 합이 총 예산보다 크면 합을 줄려야하므로 end를 mid-1
            end = mid - 1
        # print(start, end)

print(answer)