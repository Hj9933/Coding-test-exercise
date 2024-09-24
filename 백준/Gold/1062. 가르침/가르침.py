from itertools import combinations

n, k = map(int, input().split())
if k < 5:  # 'anta'와 'tica'를 읽기 위한 최소 5글자 필요
    print(0)
else:
    result = 0
    # 'antic'에 해당하는 알파벳 비트를 미리 설정
    base_mask = 0
    for char in 'antic':
        base_mask |= (1 << (ord(char) - ord('a')))
    
    word_masks = []
    for _ in range(n):
        word = input().strip()
        mask = 0
        for char in set(word) - set('antic'):
            mask |= (1 << (ord(char) - ord('a')))
        word_masks.append(mask)
    
    # 남은 알파벳 21개 중 k-5개 선택
    remaining_letters = [chr(i + ord('a')) for i in range(26) if chr(i + ord('a')) not in 'antic']
    
    max_count = 0
    for comb in combinations(remaining_letters, k - 5):
        mask = base_mask
        for char in comb:
            mask |= (1 << (ord(char) - ord('a')))
        
        count = 0
        for word_mask in word_masks:
            if word_mask & mask == word_mask:
                count += 1
        
        max_count = max(max_count, count)
    
    print(max_count)
