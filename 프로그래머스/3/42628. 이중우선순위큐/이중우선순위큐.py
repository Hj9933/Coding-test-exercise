import heapq
def solution(operations):
    q = []
    d = -1 # 최소가 디폴트
    def negative(q):
        for i in range(len(q)):
            q[i] = -q[i]
        return q
    for oper in operations:
        cmd, x = oper.split()
        x = int(x)

        if cmd == 'I':
            heapq.heappush(q, x)

        elif cmd == 'D' and x == -1:
            if len(q) > 0:
                heapq.heappop(q)
        elif cmd == 'D' and x == 1:
            if len(q) > 0:
                q = negative(q)
                heapq.heapify(q)
                heapq.heappop(q)
                q = negative(q)
                heapq.heapify(q)

    if len(q) == 0:
        answer = [0,0]
    elif len(q) == 1:
        answer = [q[0], q[0]]

    else:
        min_ans = heapq.heappop(q)
        q = negative(q)
        heapq.heapify(q)
        max_ans = -heapq.heappop(q)
        answer = [max_ans, min_ans]     
    return answer