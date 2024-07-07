from collections import Counter
def solution(want, number, discount):
    cnt_want = {}
    n_want = len(want)
    for i in range(n_want):
        cnt_want[want[i]] = number[i]
    
    result = 0
    for id in range(len(discount)-9):
        temp = Counter(discount[id:id+10])
        cnt = 0
        for k in cnt_want.keys():
            if cnt_want[str(k)] == temp.get(str(k)):
                cnt += 1    
        if cnt == len(want):
            result += 1

    return result