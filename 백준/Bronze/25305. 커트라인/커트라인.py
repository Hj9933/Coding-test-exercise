n, k = map(int, input().split())
score = list(map(int, input().split()))
# 내림차순으로 솔트 후, k번째 수를 선택
score.sort(reverse=True)
print(score[k-1])