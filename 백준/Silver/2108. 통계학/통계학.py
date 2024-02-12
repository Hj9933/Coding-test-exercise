import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = list(int(input()) for _ in range(n))

from collections import Counter
# 산술평균
print(round(sum(lst)/n)) 

# 중앙값
lst.sort()
# 홀수개면 (n+1)/2 번째가 중앙값
med_id = int((n+1)/2 - 1)
print(lst[med_id])

# 최빈값
mode_value = Counter(lst).most_common() # Counter 내장함수: 값에 개수를 연결시켜주며 최빈값 기준 정렬 후, 같으면 값이 작은 것부터 정렬됨
if len(mode_value)>1 and mode_value[0][1] == mode_value[1][1]: # 최빈값이 2개 이상이면
    print(mode_value[1][0])
else:
    print(mode_value[0][0])


# 범위
print(lst[n-1]-lst[0]) 