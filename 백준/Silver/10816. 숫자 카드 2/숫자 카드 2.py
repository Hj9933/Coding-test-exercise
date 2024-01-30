import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
lst_req = list(map(int, input().split()))

# 1. 처음에는 계수정렬로 풀려 했으나 숫자카드에 -도 있고 빈 배열의 크기가 이천만이어서 느림
# 2. 이진탐색으로 풀기 
## 이진탐색으로 찾으려는 수가 있는지 보고, 있으면 그 수가 몇개인지 카운트 -> 정렬, 이진탐색, 카운트 => 시간초과
## 이진탐색 후, 찾으려는 수가 있다면 인덱스를 앞 뒤로 움직이면서 그 수가 몇개인지 계산 -> 시간초과

# lst.sort()

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end)//2
#     if array[mid] == target:
#         i, j = 1, 1
#         while mid - i >= start: # mid를 기준으로 왼쪽으로 가면서 찾으려는 값과 같은 값 찾기
#             if lst[mid - i] != lst[mid]:
#                 break
#             else:
#                 i += 1
#         while mid + j <= end: # mid를 기준으로 오른쪽으로 가면서 찾으려는 값과 같은 값 찾기
#             if lst[mid + j] != lst[mid]:
#                 break
#             else:
#                 j += 1
#         return i + j - 1 
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
    
# for m in lst_req:
#     if binary_search(lst, m, 0, n - 1) != None:
#         print(binary_search(lst, m, 0, n - 1), end=' ')
#     else:
#         print(0, end=' ')

# dictionary 이용해서 리스트 요소와 요소 개수를 연결시켜놓은 다음, 찾으려는 값이 dict에 있으면 개수 반환 없으면 0 반환
lst.sort()
cnt = {}
for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in lst_req:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
