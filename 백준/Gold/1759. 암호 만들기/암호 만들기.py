def is_valid(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_cnt = sum(1 for c in password if c in vowels)
    consonant_cnt = len(password) - vowel_cnt
    return vowel_cnt >= 1 and consonant_cnt >= 2

def find_password(idx, password):
    if len(password) == l:
        if is_valid(password):
            print(''.join(password))
        return
    
    for i in range(idx, c):
        find_password(i+1, password+[letters[i]])



l, c = map(int, input().split())
letters = list(input().split())
letters.sort()

find_password(0, [])