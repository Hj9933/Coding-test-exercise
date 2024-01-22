import sys

n = int(sys.stdin.readline())
lst = list(sys.stdin.readline().strip() for _ in range(n))

str_dic = {}
for i in range(n):
    str_dic[lst[i]] = len(lst[i])

str_dic_sort1 = sorted(str_dic.items(), key= lambda item: (item[1], item[0]))
for i in range(len(str_dic_sort1)):
    print(str_dic_sort1[i][0])