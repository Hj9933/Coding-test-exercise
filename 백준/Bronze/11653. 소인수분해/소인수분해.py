d = 2
n = int(input())
while d <= n:
    if n % d == 0:
        print(d)
        n = n / d
    else:
        d += 1