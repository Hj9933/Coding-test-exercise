A = list(int(input()) for _ in range(10))
B = list()
for i in range(len(A)):
    B.append(A[i] % 42)

print(len(set(B)))