n = int(input())
bag = 0
while n >= 0:
    if n % 5 == 0: # 5로 나누어 떨어지면
        bag += (n//5) # 최소개수는 5로 나눈 몫
        print(bag)
        break
    n -= 3 # 5로 나누어떨어지지 않는다면 3 빼기
    bag += 1
else:
    print(-1)

    