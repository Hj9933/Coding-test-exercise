n = int(input())
for _ in range(n):
    s = list(input())
    score = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'O':
            if i >= 1 and s[i-1] == 'O':
                count += 1
            else: 
                count = 0

            if count > 0:
                score += count
            else: 
                score += 1
                count = 1
    print(score)