N = int(input())
score = list(map(int, input().split()))

max = max(score)
adj_score = []
for i in range(len(score)):
    adj_score.append(score[i]/max*100)
print(sum(adj_score)/len(adj_score))
