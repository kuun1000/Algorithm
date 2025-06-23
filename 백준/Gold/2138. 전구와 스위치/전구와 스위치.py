import sys
input = sys.stdin.readline

def flip(states, index):
    for i in [index - 1, index, index + 1]:
        if 0 <= i < len(states):
            states[i] = 1 - states[i]

def solve(states, targets):
    results = []

    for first_flip in [False, True]:
        temp_states = states.copy()
        count = 0

        if first_flip:
            flip(temp_states, 0)
            count += 1

        for i in range(1, n):
            if temp_states[i - 1] != targets[i - 1]:
                flip(temp_states, i)
                count += 1
        
        if temp_states == targets:
            results.append(count)
    
    if results:
        return min(results)
    else:
        return -1

n = int(input())
states = list(map(int, input().rstrip()))
targets = list(map(int, input().rstrip()))

print(solve(states, targets))