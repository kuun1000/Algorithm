import math

def solution(progresses, speeds):
    
    days = [math.ceil((100 - p)/s) for p, s in zip(progresses, speeds)]
    answer = []
    
    prev_day = days[0]
    count = 1
    
    for day in days[1:]:
        if prev_day >= day:
            count += 1
        else:
            answer.append(count)
            prev_day = day
            count = 1      
    answer.append(count)
    
    return answer