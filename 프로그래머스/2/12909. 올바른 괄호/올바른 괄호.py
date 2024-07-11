from collections import deque
def solution(s):
    answer = True
    s = list(s)
    len_s = len(s)
    s1 = []

    for i in range(len_s):
        if s[i] == '(':
            s1.append(s[i])
        elif s[i] == ')':
            if len(s1) > 0:
                s1.pop()
            else:
                answer = False
                break
    if len(s1) > 0:
        answer = False
    

    return answer