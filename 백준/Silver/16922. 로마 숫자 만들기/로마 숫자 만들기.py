n = int(input())

lst = [1, 5, 10, 50]

sum_lst = set()


from itertools import combinations_with_replacement

for comb in combinations_with_replacement(lst,n):
    sum_lst.add(sum(comb))

print(len(sum_lst))