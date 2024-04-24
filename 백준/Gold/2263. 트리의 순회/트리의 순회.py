import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 슬라이스를 하면 계속 새로운 리스트가 생성되어 메모리가 초과됨. 리스트가 아닌 인덱스를 넘겨주는 방식으로!

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# inorder의 index를 쉽게 알기 위한 리스트
in_id = [0]*(n+1)
for i in range(n):
    in_id[inorder[i]] = i
    
def find_preorder(left_in, right_in, left_post, right_post):
    # 후위순회를 통해 root 찾기
    if left_post > right_post:
        return
    if left_post <= right_post:
        root = postorder[right_post]
        print(root, end=' ')

        # 중위순회, 후위순회에서 root를 기준으로 왼쪽, 오른쪽 부분트리 범위 구하기
        root_id = in_id[root]
        len_left = root_id-left_in
        len_right = right_in-root_id


        # 왼쪽 부분트리부터 재귀함수를 통해 root, 좌우 부분트리 찾기 반복
        find_preorder(left_in, root_id-1, left_post, left_post+len_left-1)
        find_preorder(root_id+1, right_in, right_post-len_right, right_post-1)
    



find_preorder(0, n-1, 0, n-1)