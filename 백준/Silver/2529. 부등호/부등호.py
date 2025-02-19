def check(a, b , sign):
    return a < b if sign == '<' else a > b

def solve(depth, s):
    global max_ans, min_ans

    if depth == n + 1:
        if max_ans is None or s > max_ans:
            max_ans = s
        if min_ans is None or s < min_ans:
            min_ans = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(int(s[-1]), i, signs[depth-1]):
                visited[i] = True
                solve(depth+1, s+str(i))
                visited[i] = False


n = int(input())
signs = input().split()

visited = [False] * 10
max_ans = None
min_ans = None

solve(0, "")
print(max_ans)
print(min_ans)