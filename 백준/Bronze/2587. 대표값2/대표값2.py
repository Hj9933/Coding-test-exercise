lst = list(int(input()) for _ in range(5))

lst.sort()

print(int(sum(lst)/5))
print(lst[2])