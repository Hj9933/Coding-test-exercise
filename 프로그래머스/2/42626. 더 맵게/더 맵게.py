from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heap = scoville.copy()
    heapify(heap) # scoville을 최소heap으로 만들기
    if heap[0] >= K: # 최소값이 K 이상이면 answer=0
        answer = 0
    else: # heap의 길이가 2이상인 동안 최소값과 두번째로 작은 값을 pop하여 새로운 음식을 만든 다음 heap에 push. heap의 최소값이 K 이상이 되면 while문 종료
        flag = False # 모든 음식을 K이상으로 만들 수 없는 경우
        while len(heap) >= 2:
            answer += 1
            a = heappop(heap)
            b = heappop(heap)
            c = a + b*2
            heappush(heap, c)
            if heap[0] >= K:
                flag = True
                break

        if flag == False:
            answer = -1
    return answer