def solution(citations):
    answer = 0
    n = len(citations)
    
    citations.sort()
    
    for i in range(n):
        h = n - i
        
        if citations[i] >= h:
            answer = h
            break
        
    return answer