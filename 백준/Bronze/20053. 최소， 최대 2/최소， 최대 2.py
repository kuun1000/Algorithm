t = int(input())    # 테스트 케이스의 개수

for _ in range(t):
    n = int(input())    # 정수의 개수
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0], arr[-1])