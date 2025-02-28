n = int(input())
digit = len(str(n))

result = 0
for i in range(1, digit+1):
    if i == digit:
        result += digit*(n-10**(digit-1)+1)
    else:
        result += i*(10**(i-1)*9)
print(result)