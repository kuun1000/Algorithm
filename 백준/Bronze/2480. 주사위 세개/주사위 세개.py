dices = list(map(int, input().split()))
dices.sort()
dices_set = set(dices)

if len(dices_set) == 1:
    print(10000 + dices[0] * 1000)
elif len(dices_set) == 2:
    for i in range(3):
        cnt = dices.count(dices[i])
        if cnt == 2:
            print(1000 + dices[i] * 100)
            break
else:
    print(max(dices) * 100)