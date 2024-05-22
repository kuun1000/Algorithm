def solution(arr):
    stack = []
    result = [arr[0]]
    
    for elem in arr:
        if len(stack) != 0:
            curr = stack.pop()
            if curr != elem:
                result.append(elem)
                
        stack.append(elem)
        
    return result