def combination(seq, start):
    if len(seq) == 6:
        print(*seq)
        return
    
    for i in range(start, len(s)):
        combination(seq+[s[i]], i+1)

    

while True:
    array = list(map(int, input().split()))
    k, s = array[0], array[1:]
    
    if k == 0:
        break
    
    combination([], 0)
    print()