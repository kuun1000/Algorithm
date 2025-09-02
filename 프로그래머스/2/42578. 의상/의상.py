def solution(clothes):
    
    d = {}
    for n, t in clothes:
        if t in d:
            d[t].append(n)
        else:
            d[t] = [n]
    
    answer = 1
    for _, value in d.items():
        answer *= len(value)+1
        
    return answer - 1