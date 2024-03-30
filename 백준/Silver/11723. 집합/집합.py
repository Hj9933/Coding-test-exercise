import sys

n = int(sys.stdin.readline())

S = set()
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'add':
        S.add(int(command[1]))
    elif command[0] == 'remove':
        S.discard(int(command[1])) # remove가 아닌 discard로 해야 없는 원소 제거할 때 에러 안남
    elif command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.discard(int(command[1]))
        else: 
            S.add(int(command[1]))
    elif command[0] == 'all':
        S = set([i for i in range(1, 21)])
    elif command[0] == 'empty':
        S = set()
        
    