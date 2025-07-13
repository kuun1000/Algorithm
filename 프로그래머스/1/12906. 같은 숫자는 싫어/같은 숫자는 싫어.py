def solution(arr):
    answer = []
    current = arr[0]
    
    for elem in arr:
        if not answer or elem != current:
            answer.append(elem)
            current = elem
            
    return answer