# 과일 탕후루
n = int(input())
lst = list(map(int, input().split()))
fruit_cnt = {}
left = 0
max_len = 0
for right in range(n):
    current = lst[right]
    if current in fruit_cnt:
        fruit_cnt[current] += 1
    else:
        fruit_cnt[current] = 1
    
    while len(fruit_cnt) > 2:
        rm = lst[left]
        fruit_cnt[rm] -= 1
        if fruit_cnt[rm] == 0:
            del fruit_cnt[rm]
        left += 1
        if left >= n:
            break

    max_len = max(max_len, right-left+1)
print(max_len)