from collections import Counter

def solution(nums):
    
    max_select = len(nums) / 2
    ponketmon = Counter(nums)
    
    if max_select < len(ponketmon):
        return max_select
    else:
        return len(ponketmon)