# 1339. 단어수학
n = int(input())
words = {}
S = [list(input()) for _ in range(n)]
for s in S:
    m = len(s)-1
    for i in s:
        if i in words:
            words[i] += 10**m
        else:
            words[i] = 10**m
        m -= 1
words_sorted = sorted(words.values(),reverse=True)
result = 0
num = 9
for k in words_sorted:
    result += k*num
    num -= 1
print(result)