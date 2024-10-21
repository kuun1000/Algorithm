arr = set([int(input()) for _ in range(28)])
num = set([i for i in range(1, 31)])

remain = list(num - arr)
remain.sort()

for r in remain:
    print(r)