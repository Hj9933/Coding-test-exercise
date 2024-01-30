import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

A.sort()
for i in lst:
    if binary_search(A, i, 0, n-1) != None:
        print(1)
    else:
        print(0)