import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

a_1 = A-B
b_1 = B-A
print(len(a_1|b_1))