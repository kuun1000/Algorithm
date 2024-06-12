import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # 현재 값보다 큰 값을 가지는 데이터 제거
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    # 덱의 마지막 위치에 현재 값 데이터 저장
    mydeque.append((now[i], i))
    # 슬라이딩 윈도우 범위 벗어난 데이터 제거
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    # 덱의 1번째 데이터 출력
    print(mydeque[0][0], end=" ")