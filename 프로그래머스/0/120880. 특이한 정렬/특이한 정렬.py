def solution(numlist, n):
    lst = []
    for i in numlist:
        lst.append([i, abs(n-i)])  
    lst.sort(key = lambda x: (x[1], -x[0]))
    answer = []
    for i in lst:
        answer.append(i[0])
    return answer