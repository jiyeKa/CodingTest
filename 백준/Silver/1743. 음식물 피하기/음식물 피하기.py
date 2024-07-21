import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  cnt = 0  
  q = deque()
  q.append((x, y))
  graph[x][y] = 0

  while q:
    x, y = q.popleft()
    cnt += 1 
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if(0<=nx<N and 0<=ny<M):
        if(graph[nx][ny]==1):
          q.append((nx,ny))
          graph[nx][ny]=0
  return cnt       

N, M, K = map(int, sys.stdin.readline().split())
size = []  
graph = [[0 for _ in range(M)] for _ in range(N)]  

for _ in range(K):
  r, c = map(int, sys.stdin.readline().split())
  graph[r - 1][c - 1] = 1  


for i in range(N):
  for j in range(M):
    if(graph[i][j] == 1):
      size.append(bfs(i, j))

print(max(size))