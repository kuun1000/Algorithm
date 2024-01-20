t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    
    p = ""
    for elem in s:
        p += elem * r
    
    print(p)
    