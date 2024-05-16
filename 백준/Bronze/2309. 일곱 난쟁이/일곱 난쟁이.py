from itertools import combinations
heights = list(int(input()) for _ in range(9))

for comb in combinations(heights, 7):
    s = sum(comb)
    if s == 100:
        for c in sorted(comb):
            print(c)
        break