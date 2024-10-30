n = int(input())
members = [[int(age), name, i] for i, (age, name) in enumerate(input().split() for _ in range(n))]

members.sort(key=lambda members:(members[0], members[2]))

for member in members:
    print(member[0], member[1])