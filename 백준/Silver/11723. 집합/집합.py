import sys

input = sys.stdin.readline
S = 0  

output = []

for _ in range(int(input().strip())):
    command = input().strip().split()
    if command[0] == "add":
        S |= (1 << (int(command[1]) - 1))
    
    elif command[0] == "remove":
        S &= ~(1 << (int(command[1]) - 1))
    
    elif command[0] == "check":
        sys.stdout.write("1\n" if (S & (1 << (int(command[1]) - 1))) else "0\n")
    
    elif command[0] == "toggle":
        S ^= (1 << (int(command[1]) - 1))
    
    elif command[0] == "all":
        S = (1 << 20) - 1
    
    elif command[0] == "empty":
        S = 0