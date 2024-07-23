import sys

def dfs(c):
    if c == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N + 1):
        arr[c] = i
        dfs(c + 1)

N, M = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(M)]
dfs(0)