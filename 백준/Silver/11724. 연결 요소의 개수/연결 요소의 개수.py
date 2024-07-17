import sys

def dfs(x):
    visited[x]=True
    for i in range(1,N+1):
        if not visited[i] and graph[x][i]:
            dfs(i)    

N,M=map(int,sys.stdin.readline().split())
graph=[[0 for _ in range(N+1)] for _ in range(N+1)]
visited=[False]*(N+1)

for i in range(M):
    v1,v2=map(int,sys.stdin.readline().split())
    graph[v1][v2]=1
    graph[v2][v1]=1

count=0
for x in range(1,N+1):
    if not visited[x]:
        count+=1
        dfs(x)

print(count)