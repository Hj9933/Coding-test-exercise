from collections import deque

n = int(input())
for i in range(n):
    n_doc, curious = map(int, input().split())
    lst = list(map(int, input().split()))
    deq = deque(lst)
    count = 0 # 인쇄된 횟수
    while True:
        if len(deq) > 0 and deq[0] != max(deq): # 큐의 첫번째 원소가 최대값이 아니라면 왼쪽에서 빼서 오른쪽으로 붙이기
            deq.append(deq.popleft())
            curious -= 1 # 궁금한 문서의 인덱스도 같이 옮겨야 함
            if curious < 0: # 만일 인덱스가 음수가 된다면 맨 끝 인덱스로 옮겨야 함
                curious += len(deq)
        elif len(deq) > 0 and deq[0] == max(deq): # 최대값이 맞다면 인쇄, 즉 popleft
            if curious == 0: # 궁금한 인덱스가 0번째면 인쇄할 문서가 궁금한 문서라는 것이므로 count에 1을 더해 출력하고 반복문 마침
                count += 1
                print(count)
                break
            else: # 궁금한 인덱스가 0이 아니라면 그냥 인쇄. 즉 popleft하고 인덱스 하나씩 밀리므로 궁금한 인덱스도 -1
                deq.popleft()
                count += 1
                curious -= 1
        if len(deq) == 0:
            break
