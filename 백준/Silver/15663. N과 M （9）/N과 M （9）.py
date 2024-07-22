import sys

def dfs():
    if len(answer) == M:
        print(*answer)
        return
    check = 0
    for i in range(N):
        if not visited[i] and check != nums[i]:
            visited[i] = True
            answer.append(nums[i])
            check = nums[i]
            dfs()
            visited[i] = False
            answer.pop()

N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * N
answer = []
dfs()