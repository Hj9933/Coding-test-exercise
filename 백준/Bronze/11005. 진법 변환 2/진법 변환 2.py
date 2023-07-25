n, b = map(int, input().split())
digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z")

res = ''
while n > 0:
    n, r = divmod(n, b)
    res = digits[r] + res

print(res)