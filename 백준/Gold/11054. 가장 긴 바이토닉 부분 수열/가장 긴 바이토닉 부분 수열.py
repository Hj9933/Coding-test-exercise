# 가장 긴 바이토닉 수열
n = int(input())
lst = list(map(int, input().split()))
dp_inc = [1]*n
dp_dec = [1]*n
reverse_lst = lst[::-1]

for i in range(n):
    for j in range(i):
        # 증가하는 수열열
        if lst[i] > lst[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)
        # 감소하는 수열
        if reverse_lst[i] > reverse_lst[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j]+1)

dp_dec = dp_dec[::-1]
result = 0
for i in range(n):
    tmp = dp_dec[i]+dp_inc[i]-1
    result = max(result, tmp)
print(result)