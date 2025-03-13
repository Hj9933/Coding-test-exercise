# 팰린드롬 만들기
words = list(input())
A = [] # 앞 문자열
B = [] # 대응되는 뒷 문자열
C = [] # 길이가 홀수라면 가운데 오는 문자

words.sort()
dic = {}
for w in words:
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1
flag = False
answer = 0
for w in dic:
    if dic[w] % 2 == 0: # 짝수면 대응되는 문자가 있다는것
        A.append(w*int(dic[w]/2))
        B.append(w*int(dic[w]/2))
    elif dic[w] %2 != 0 and not flag:
        A.append(w*int(dic[w]/2))
        B.append(w*int(dic[w]/2))
        C.append(w)
        flag = True
    else:
        answer = "I'm Sorry Hansoo"

if answer == 0:
    B.reverse()
    answer = ''.join(A+C+B)
    print(answer)
else:
    print(answer)
