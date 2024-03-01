n = int(input())

fee = [[0,0,0]]
for i in range(n):
    fee.append(list(map(int, input().split())))
# R,G,B 각각에 대한 비용

pay = [[0,0,0] for _ in range(n+1)]
pay[1] = fee[1]

for i in range(2, n+1):
    pay[i][0] = fee[i][0] + min(pay[i-1][1], pay[i-1][2])
    pay[i][1] = fee[i][1] + min(pay[i-1][0], pay[i-1][2])
    pay[i][2] = fee[i][2] + min(pay[i-1][0], pay[i-1][1])    

print(min(pay[n]))