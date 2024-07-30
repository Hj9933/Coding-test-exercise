import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

b,w = 0,0
def cut(paper, r, c):
    paper_temp1 = paper[0:int(r/2)]
    paper1 = []
    paper2 = []
    for i in range(0,int(r/2)):
        paper1.append(paper_temp1[i][0:int(c/2)])
        paper2.append(paper_temp1[i][int(c/2):c])
    paper_temp2 = paper[int(r/2):r]
    paper3 = []
    paper4 = []
    for i in range(0,int(r/2)):
        paper3.append(paper_temp2[i][0:int(c/2)])
        paper4.append(paper_temp2[i][int(c/2):c])
    return paper1, paper2, paper3, paper4

def perform(paper, n):
    global result_b, result_w
    b, w = 0,0
    for i in range(n):
        for j in range(n):
            if paper[i][j] == 1:
                b += 1
            else:
                w += 1
    if b != n*n and w!=n*n:
        paper1, paper2, paper3, paper4 = cut(paper, n, n)
        perform(paper1,int(n/2))
        perform(paper2,int(n/2))
        perform(paper3,int(n/2))
        perform(paper4,int(n/2))
    elif b == n*n:
        result_b += 1
    elif w == n*n:
        result_w += 1
result_w, result_b = 0,0
perform(paper,n)
print(result_w)
print(result_b)