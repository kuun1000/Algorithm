n, m = tuple(map(int, input().split()))

# 각 바구니에 들어있는 공의 번호
arr = [i for i in range(1, n+1)]

# m개의 명령에 대해 
for _ in range(m):
    # 명령을 입력 받아
    i, j = tuple(map(int, input().split()))
    
    # i-1번째와 j-1번째 원소를 교환
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

print(*arr)