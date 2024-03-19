def solution(answers):
    n_prob = len(answers)
    one_pattern = [1,2,3,4,5]
    one = one_pattern*(n_prob//5)
    if n_prob%5 != 0:
        one.extend(one_pattern[:n_prob%5])
    two_pattern = [2,1,2,3,2,4,2,5]
    two = two_pattern*(n_prob//8)
    if n_prob%8 != 0:
        two.extend(two_pattern[:n_prob%8])
    three_pattern = [3,3,1,1,2,2,4,4,5,5]
    three = three_pattern*(n_prob//10)
    if n_prob%10 != 0:
        three.extend(three_pattern[:n_prob%10])
    
    cor_one = 0
    for i in range(len(answers)):
        if answers[i] == one[i]:
            cor_one += 1
    cor_two = 0
    for i in range(len(answers)):
        if answers[i] == two[i]:
            cor_two += 1
    cor_three = 0
    for i in range(len(answers)):
        if answers[i] == three[i]:
            cor_three += 1
    cor = [cor_one, cor_two, cor_three]
    max_cor = max(cor)
    answer = []
    for i in range(3):
        if cor[i] == max_cor:
            answer.append(i+1)
        
    return answer
