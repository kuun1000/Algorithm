croatians = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input()
for croatian in croatians:
    s = s.replace(croatian, '*')
print(len(s))