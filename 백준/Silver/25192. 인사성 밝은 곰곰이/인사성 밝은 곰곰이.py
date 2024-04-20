n = int(input())
result = 0
person = {}
for _ in range(n):
    char = input()
    if char == 'ENTER':
        result += sum(person.values())
        person = {}
    else:
        if char not in person:
            person[char] = 1
result += sum(person.values())

print(result)