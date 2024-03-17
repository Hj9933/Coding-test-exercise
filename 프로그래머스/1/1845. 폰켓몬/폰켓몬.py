def solution(nums):
    answer = 0
    n = len(nums)
    num_set = set(nums)
    if n/2 >= len(num_set):
        answer = len(num_set)
    else:
        answer = n/2
    
    return answer