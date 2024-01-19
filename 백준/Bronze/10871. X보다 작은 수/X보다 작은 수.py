# 입력 받기
n, x = tuple(map(int, input().split()))
a = list(map(int, input().split()))

# 수열의 모든 원소에 대해
for elem in a:
    # 해당 원소가 x보다 작은 경우
    if elem < x:
        print(elem, end=" ")