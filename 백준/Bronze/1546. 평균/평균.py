n = int(input())
score = list(map(int, input().split()))

# 최대 점수
max_val = max(score)

# 점수 조작
manipulated = [(elem / max_val * 100) for elem in score]

# 평균 계산
print(sum(manipulated) / n)