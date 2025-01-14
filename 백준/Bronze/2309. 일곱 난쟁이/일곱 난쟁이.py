dwarf = [int(input()) for _ in range(9)]


total = sum(dwarf)

found = False
for i in range(9):
    for j in range(i+1, 9):
        if total - (dwarf[i] + dwarf[j]) == 100:
            result = [dwarf[k] for k in range(9) if k != i and k != j]
            found = True
            break
    if found:
        break

result.sort()
for height in result:
    print(height)