def solution(clothes):
    answer = 0
    dict = {}
    for clothe in clothes:
        if clothe[1] in dict.keys():
            dict[clothe[1]] += 1
        else:
            dict[clothe[1]] = 1
    answer = 1
    for dic in dict.values():
        answer = answer*(dic+1)
    answer -= 1
    return answer