from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
sym_cnt = list(map(int, input().split()))

sym = ['+'] * sym_cnt[0] + ['-'] * sym_cnt[1] + ['x'] * sym_cnt[2] + ['%'] * sym_cnt[3]

result_max = -int(1e9)
result_min = int(1e9)

for perm in permutations(sym, n-1):
    temp = 0
    for i in range(n-1):
        if perm[i] == '+':
            if i == 0:
                temp += nums[i] + nums[i+1]
            else:
                temp +=nums[i+1]
        elif perm[i] == '-':
            if i == 0:
                temp += nums[i] - nums[i+1]
            else:
                temp -= nums[i+1]
        elif perm[i] == 'x':
            if i == 0:
                temp += nums[i]*nums[i+1]
            else:
                temp *= nums[i+1]
        elif perm[i] == '%':
            if i == 0:
                if nums[i] < 0 and nums[i+1] > 0:
                    temp += -((-nums[i])//nums[i+1])
                else:
                    temp += nums[i]//nums[i+1]
            else:
                if temp < 0 and nums[i+1] > 0:
                    temp = -((-temp)//nums[i+1])
                else:
                    temp = temp//nums[i+1]
    
    result_max = max(result_max, temp)
    result_min = min(result_min, temp)

print(result_max)
print(result_min)