from itertools import permutations
import math
def solution(numbers):
    answer = 0
    nums = list(numbers)
    result = []
    n = len(nums)
    for i in range(1, n+1):
        for perm in permutations(nums,i):
            if perm[0] != "0":
                tmp = int("".join(perm))
                flag = False
                if tmp != 1 and tmp not in result:
                    result.append(tmp)
                    for j in range(2, int(math.sqrt(tmp)+1)):
                        if tmp%j == 0:
                            flag = True
                    if flag == False:
                        answer += 1
                    
    return answer