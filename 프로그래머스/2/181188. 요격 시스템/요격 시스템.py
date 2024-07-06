def solution(targets):
    answer = 0
    targets.sort(key = lambda x: x[1])
    check = -1
    for i in range(len(targets)):
        if check <= targets[i][0]:
            check = targets[i][1]
            answer +=1
    return answer