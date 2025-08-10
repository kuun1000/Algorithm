import sys
input = sys.stdin.readline

n = int(input())
n_set = set(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

for elem in m_arr:
    print(1 if elem in n_set else 0)