h, m = map(int, input().split())
a = int(input())  

if m + a < 60:
    print(h, m + a)
elif ((h + ((m + a) // 60)) <= 23) & ((m + a) >= 60):
    print(h + ((m + a) // 60), (m + a) % 60)
elif ((h + ((m + a) // 60)) > 23) & ((m + a) >= 60):
    print((h + (m + a) // 60) - 24, (m + a) % 60)