def recursion(n):
    if n == 1:
        return 3
    return recursion(n-1)*2-1

n = int(input())
print(recursion(n)**2)