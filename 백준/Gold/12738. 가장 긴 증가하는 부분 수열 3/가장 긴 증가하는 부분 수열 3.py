n = int(input())
A = list(map(int, input().split()))
INF = 10e9
lst = [-INF]
for a in A:
    if a > lst[-1]:
        lst.append(a)
    elif a <= lst[1]:
        lst[1] = a
    else:
        low = 0
        high = len(lst)-1
        while low <= high:
            mid = (low+high)//2
            if lst[mid] < a:
                low = mid+1
            else:
                high = mid-1
        lst[low] = a

print(len(lst)-1)