n = int(input())
i = 0
start = 1

while (True):
    if n > start:
        i += 1
        start += i*6
    else:
        print(i + 1)
        break