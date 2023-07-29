for _ in range(int(input())):
    t = int(input())

    q, r = divmod(t, 25)
    d, r = divmod(r, 10)
    n, r = divmod(r, 5)
    p, r = divmod(r, 1)

    print(int(q), int(d), int(n), int(p))