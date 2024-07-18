import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):           
    q = [(x,y)]
    graph[x][y] = 0

    while q:
        x,y = q.pop(0)
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if x1 < 0 or x1 >= M or y1 < 0 or y1 >= N:
                continue
            if graph[x1][y1] == 1 :
                q.append((x1,y1))
                graph[x1][y1] = 0

T=int(sys.stdin.readline())

for i in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    graph = [[0]*(N) for _ in range(M)]
    count = 0
    for j in range(K):
        x,y = map(int, input().split())
        graph[x][y] = 1
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                bfs(x,y)
                count += 1
    print(count)