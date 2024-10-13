def solution(number, k):
    arr = []
    for word in number:
        while arr and arr[-1] < word and k > 0:
            arr.pop()
            k -= 1
        arr.append(word)
    if k > 0:
        answer = ''.join(map(str, arr[:-k]))
    else:
        answer = ''.join(map(str,arr))
    return answer