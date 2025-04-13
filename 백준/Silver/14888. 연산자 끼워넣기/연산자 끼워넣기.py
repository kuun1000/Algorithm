import sys
input = sys.stdin.readline


def backtrack(idx, result, plus, minus, mul, div):
    if idx == n:
        global max_result, min_result
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    if plus > 0:
        backtrack(idx+1, result + sequence[idx], plus-1, minus, mul, div)
    if minus > 0:
        backtrack(idx+1, result - sequence[idx], plus, minus-1, mul, div)
    if mul > 0:
        backtrack(idx+1, result * sequence[idx], plus, minus, mul-1, div)
    if div > 0:
        next_result = result // sequence[idx] if result > 0 else -(abs(result) // sequence[idx])
        backtrack(idx+1, next_result, plus, minus, mul, div-1)

n = int(input())
sequence = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_result, min_result = -sys.maxsize, sys.maxsize

backtrack(1, sequence[0], *operations)
print(max_result)
print(min_result)