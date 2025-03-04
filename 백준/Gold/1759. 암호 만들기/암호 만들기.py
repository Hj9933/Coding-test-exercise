l, c = map(int, input().split())
alphabets = list(input().split())

aeiou = ['a','e','i','o','u']
a = [] # 모음만 저장
b = [] # 자음만 저장
for i in alphabets:
    if i in aeiou:
        a.append(i)
    else:
        b.append(i)
alphabets = set(alphabets)
from itertools import combinations
answers = set()
for As in combinations(a,1):
    result = set()
    result.add(*As)
    for Bs in combinations(b,2):
        result1 = set()
        result1 = result.union(set(Bs))
        for Cs in combinations(alphabets-result1,l-3):
            answer = sorted(result1.union(set(Cs)))
            answer = ''.join(answer)
            answers.add(answer)
answers = sorted(list(answers))
for k in answers:
    print(k)