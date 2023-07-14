t = int(input())
str = [input() for _ in range(t)]
for i in range(t):
    print(str[i][0], str[i][len(str[i])-1], sep='')