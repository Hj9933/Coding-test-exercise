from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for perm in permutations(dungeons, len(dungeons)):
        cnt = 0
        remaining_k = k
        for need, use in perm:
            if remaining_k >= need:
                remaining_k -= use
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    return answer