a = [int(input()) for _ in range(28)]
l = [i for i in range(1,31)]

no = set(l)-set(a)
no_list = [i for i in no]
no_list.sort()

for i in range(len(no_list)):
    print(no_list[i])