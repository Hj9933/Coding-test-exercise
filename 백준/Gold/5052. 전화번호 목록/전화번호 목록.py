import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phone_book = [str(input().strip()) for _ in range(n)]
    answer = "YES"
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = "NO"
            break
    print(answer)