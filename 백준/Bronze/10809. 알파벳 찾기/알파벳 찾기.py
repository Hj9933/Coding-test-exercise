s = list(input())

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

a = []
for i in range(len(alphabet)):
    if alphabet[i] not in s:
        a.append(-1)
    else:
        for j in range(len(s)):
            if (s[j] == alphabet[i]) & (s[0:j+1].count(alphabet[i]) == 1):
                a.append(j)

for i in range(len(a)):
    print(a[i], end = " ")
