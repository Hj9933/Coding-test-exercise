import sys
input = sys.stdin.readline
# 두 배열의 합
t = int(input())
n_a = int(input())
A = list(map(int, input().split()))
n_b = int(input())
B = list(map(int, input().split()))
sum_a = [] # A의 누적합
for i in range(n_a):
    for j in range(i+1, n_a+1):
        sum_a.append(sum(A[i:j]))
sum_b = []
for i in range(n_b):
    for j in range(i+1, n_b+1):
        sum_b.append(sum(B[i:j]))
sum_a.sort()
sum_b.sort()
answer = 0
import bisect
for i in range(len(sum_a)): # sum_b에 t-sum_a[i]가 있다면 l과 r의 값이 있을 것이고 결국 r-l은 그 개수를 알려줌. 값이 없다면 l과 r의 값은 같을 것이므로 빼면 0
    l = bisect.bisect_left(sum_b, t-sum_a[i])
    r = bisect.bisect_right(sum_b, t-sum_a[i])
    answer += r-l
print(answer)