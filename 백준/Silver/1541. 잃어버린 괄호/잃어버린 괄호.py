formula = input()

# 식에 -와 +가 섞여있다면, +로 연결된 식에 무조건 괄호
formula = formula.split('-')
formula1 = []
for i in formula:
    if '+' in i:
        s = list(map(int,i.split('+')))
        formula1.append(sum(s))
    else:
        formula1.append(int(i))
result = int(formula1.pop(0))
for i in formula1:
    result -= i
print(result)