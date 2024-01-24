def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True, key = lambda x: (x*4)[:4])
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer
