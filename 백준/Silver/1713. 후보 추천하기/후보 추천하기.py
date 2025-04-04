# 후보 추천하기
from collections import deque
n = int(input())
T = int(input())
lst = list(map(int,input().split()))

dic = {}
recommend = []
cnt = 0

for i in lst:
    if cnt < n:
        if i not in dic:
            dic[i] = 1
            recommend.append(i)
            cnt += 1
        else:
            dic[i] += 1
    else:
        if i not in dic:
            min_lst = [k for k, v in dic.items() if min(dic.values()) == v]
            for r in recommend:
                if r in min_lst:
                    recommend.remove(r)
                    dic.pop(r)
                    recommend.append(i)
                    dic[i] = 1
                    break
        else:
            dic[i] += 1
        
recommend.sort()
print(*recommend)
