import sys
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not arr[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

N,M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()
result = 0

for x in range(N):
    for y in range(M):
        if arr[x][y]:
            q.append((x, y))
bfs()
for a in arr:
    result = max(max(a), result)
print(result - 1)