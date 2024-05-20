def solution(nums):
    N = len(nums)   # 총 포켓몬 수
    answer = len(set(nums)) # 포켓몬 종류의 수
    
    # 포켓몬 종류의 수 > 최대로 선택 가능한 포켓몬 수 -> N/2 마리
    if answer > N/2:    
        return N/2
    
    # 포켓몬 종류의 수 <= 최대로 선택 가능한 포켓몬 수 ->  포켓몬 종류의 수
    return answer   