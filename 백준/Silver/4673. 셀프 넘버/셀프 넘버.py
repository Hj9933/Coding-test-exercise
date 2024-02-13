self_num_lst = [0]*10036
for i in range(10000): # 생성자를 0부터 9999까지 -> 생성자가 9999일 때, 최대 셀프넘버 10035
    num = i+1 # 생성자
    sevaral_num = list(str(num)) # 생성자를 각 자릿수별로 나누어 리스트로 저장
    self_num = num
    for j in sevaral_num:
        self_num += int(j) # 셀프넘버 생성
    self_num_lst[self_num] += 1 # 셀프넘버에 해당하는 인덱스에 +1
# 리스트에서 값이 0인 인덱스가 셀프넘버가 아닌 숫자
for i in range(len(self_num_lst)):
    if i != 0 and self_num_lst[i] == 0 and i < 10000:
        print(i)