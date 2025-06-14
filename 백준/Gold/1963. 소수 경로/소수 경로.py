from math import sqrt
from collections import deque
import sys
input = sys.stdin.readline

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def get_neighbors(num, primes):
    neighbors = []
    num_str = str(num)

    for i in range(4):
        for digit in '0123456789':
            if i == 0 and digit == '0':
                continue
            if num_str[i] == digit:
                continue

            candidate = list(num_str)
            candidate[i] = digit
            new_num = int(''.join(candidate))

            if new_num in primes:
                neighbors.append(new_num)
    
    return neighbors

def bfs(start, target, primes_set):
    visited = [-1] * 10000
    queue = deque()

    visited[start] = 0
    queue.append(start)

    while queue:
        current = queue.popleft()

        if current == target:
            return visited[current]
        
        for neighbor in get_neighbors(current, primes_set):
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    
    return 'Impossible'


t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]

primes = [i for i in range(1000, 10000) if is_prime(i)]
primes_set = set(primes)

for a, b in cases:
    print(bfs(a, b, primes_set))