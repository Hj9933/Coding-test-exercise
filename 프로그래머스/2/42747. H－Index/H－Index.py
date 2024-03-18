def solution(citations):
    citations.sort() # 인용 수 기준으로 정렬
    h_max = citations[-1]
    for i in range(h_max+1):
        sum = 0
        for j in citations:
            if j >= i:
                sum += 1
        if sum >= i:
            h = i
            
    return h