def solution(balls, share):
    denom = 1
    num = 1
    
    for i in range(balls, 0, -1):
        denom *= i
        
    for j in range((balls - share), 0, -1):
        num *= j
    
    for k in range(share, 0, -1):
        num *= k
    
    return denom / num