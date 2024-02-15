import sys
input = sys.stdin.readline

from collections import Counter
import math
num = list(input())

# 6과 9는 같은 카드로 보면 되므로 모두 6으로 통일. 즉, 9가 나오면 6으로 바꿔주기
for i in range(len(num)):
    if num[i] == '9':
        num[i] = '6'
# 카드들 중 최빈값을 찾아 그 개수만큼 세트를 사면 됨. 단, 6이 최빈값이라면 개수/2를 올림한 만큼 사야되므로 두번째 최빈값가 비교하여 더 큰 개수만큼 사기
mode_value = Counter(num).most_common()
if mode_value[0][0] != '6': # 최빈값인 카드가 6이 아니면 그대로 개수 출력
    print(mode_value[0][1])
else: # 최빈값인 카드가 6이라면 개수/2를 올림한 수와 두번째 최빈값의 개수를 비교해서 더 큰 값을 출력
    if int(math.ceil(mode_value[0][1]/2)) >= mode_value[1][1]:
        print(int(math.ceil(mode_value[0][1]/2)))
    else:
        print(mode_value[1][1])


