a = list(input())

dial = []
dial.append([chr(i) for i in range(ord('A'), ord('C')+1)])
dial.append([chr(i) for i in range(ord('D'), ord('F')+1)])
dial.append([chr(i) for i in range(ord('G'), ord('I')+1)])
dial.append([chr(i) for i in range(ord('J'), ord('L')+1)])
dial.append([chr(i) for i in range(ord('M'), ord('O')+1)])
dial.append([chr(i) for i in range(ord('P'), ord('S')+1)])
dial.append([chr(i) for i in range(ord('T'), ord('V')+1)])
dial.append([chr(i) for i in range(ord('W'), ord('Z')+1)])

time = 0
for i in range(len(a)):
    for j in range(len(dial)):
        if a[i] in dial[j]:
            time += (j + 3)
    
print(time)