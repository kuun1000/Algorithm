H, M = tuple(map(int, input().split()))

if M < 45:
    M = M + 60 - 45
    if H == 0:
        H = 23
    else:
        H -= 1
else:
    M -= 45

print(f"{H} {M}")