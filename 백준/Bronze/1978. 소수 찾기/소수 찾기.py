n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for num in arr:
    for i in range(2, num+1):
        if num % i == 0:
            if num == i:
                cnt += 1
            break
print(cnt)