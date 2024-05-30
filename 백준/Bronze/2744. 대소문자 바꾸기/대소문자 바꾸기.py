lst = list(input())

answer = ''
for i in lst:
    if i.isupper() == True:
        answer = answer + i.lower()
    else:
        answer = answer + i.upper()

print(answer)