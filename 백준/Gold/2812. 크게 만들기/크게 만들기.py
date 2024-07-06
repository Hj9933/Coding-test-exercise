n, k = map(int, input().split())
num = list(str(input()))

arr = []
for w in num:
    while arr and arr[-1] < int(w) and k > 0:
        arr.pop()
        k -= 1
    arr.append(int(w))

if k > 0:
    print(''.join(map(str, arr[:-k])))
else:
    print(''.join(map(str, arr)))