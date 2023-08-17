while True:
    inp = list(map(int, input().split()))
    inp1 = inp.copy()
    if inp[0] == inp[1] and inp[1] == inp[2] and inp[0] == 0:
        break
    m = max(inp)
    inp1.remove(m)
    if max(inp) >= sum(inp1):
        print('Invalid')
    elif inp[0] == inp[1] and inp[1] == inp[2]:
        print('Equilateral')
    elif inp[0] != inp[1] and inp[1] != inp[2] and inp[0] != inp[2]:
        print('Scalene')
    elif (inp[0] == inp[1] and inp[1] != inp[2]) or (inp[1]==inp[2] and inp[0]!=inp[1]) or (inp[0]==inp[2] and inp[1]!=inp[2]):
        print('Isosceles')
