n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key = lambda x: (x[1], x[0])) # 끝나는 시간 기준 정렬 후, 시작 시간 기준 정렬

count = 1 # 맨 첫 원소는 무조건 포함
i = 0
while i < n-1:
    j = i + 1 # 인덱스 저장
    while True: # 끝 시간과 시작시간이 겹치지 않을 때까지 i에 1 더해서 인덱스 뒤로 보내기
        if lst[i][1] > lst[j][0]: # 끝 시간이 시작시간보다 크면 겹치는 것이므로 i에 1더하기
            j += 1
            if j > n-1:
                break
        else: # 끝 시간이 시작시간보다 같거나 작으면 겹치지 않는 것이므로 count에 1 더하고 j에 1더함
            count += 1
            break
    i = j    
print(count)