import math
def solution(n, times):
    answer = 0
    per = len(times)

    # 시간을 기준으로 이분탐색
    # 걸릴 수 있는 최대시간은 times[0]*n
    start = 0
    end = int(1e20)
    cnt = 0
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        comp_min = int(1e18)
        for t in times:
            a, b = divmod(mid, t)
            cnt += a
            comp_min = min(b, comp_min)
        if cnt == n:
            break
        elif cnt > n:
            end = mid - 1
        else:
            start = mid + 1

    if comp_min==0:
        answer = mid
    else:
        answer = mid - comp_min

    return answer