import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]

essential = {'a', 'n', 't', 'i', 'c'}
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

stripped_words = []
unique_chars = set()

for word in words:
    core = set(word[4:-4]) - essential
    stripped_words.append(core)
    unique_chars |= core

candidates = list(unique_chars)
visited = [False] * 26
max_count = 0

# 기본 문자 마킹
for ch in essential:
    visited[ord(ch) - ord('a')] = True

def count_readable():
    count = 0
    for word_set in stripped_words:
        if all(visited[ord(ch) - ord('a')] for ch in word_set):
            count += 1
    return count

def backtrack(start, depth):
    global max_count
    if depth == K - 5:
        max_count = max(max_count, count_readable())
        return
    for i in range(start, len(candidates)):
        ch = candidates[i]
        idx = ord(ch) - ord('a')
        if not visited[idx]:
            visited[idx] = True
            backtrack(i + 1, depth + 1)
            visited[idx] = False

# 후보가 배울 수 있는 수보다 적으면 그냥 다 배움
if len(candidates) <= K - 5:
    for ch in candidates:
        visited[ord(ch) - ord('a')] = True
    print(count_readable())
else:
    backtrack(0, 0)
    print(max_count)