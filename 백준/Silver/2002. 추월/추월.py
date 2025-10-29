n = int(input())
dic = {}

for i in range(n):
    dic[input()]=i
out_car = []
for _ in range(n):
    car = input()
    out_car.append(dic[car])

cnt = 0
for i in range(n):
    for j in range(i,n):
        if out_car[i] > out_car[j]:
            cnt += 1
            break
print(cnt)

