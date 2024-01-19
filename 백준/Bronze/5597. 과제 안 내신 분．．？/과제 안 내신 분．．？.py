# 전체 출석번호 배열
nums = [i for i in range(1, 31)]

# 28명의 출석번호에 대해
for _ in range(28):
    # 전체에서 해당 출석번호 제거
    nums.remove(int(input()))

# 오름차순 정렬
nums.sort()

for elem in nums:
    print(elem)