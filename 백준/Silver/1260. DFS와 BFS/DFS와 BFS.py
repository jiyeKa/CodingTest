import sys
from collections import deque

def DFS(V):
    DFSvisited[V]=True
    print(V,end=" ")
    for i in range(1,N+1):
        if DFSvisited[i]==False and graph[V][i]==1:
            DFS(i)
    
def BFS(V):
    q=deque([V])
    BFSvisited[V]=True
    while q:
        V=q.popleft()
        print(V,end=" ")
        for i in range(1,N+1):
            if BFSvisited[i]==False and graph[V][i]==1:
                q.append(i)
                BFSvisited[i]=True

N,M,V=map(int,sys.stdin.readline().split())

graph=[[0 for j in range(N+1)] for i in range(N+1)]
DFSvisited=[False for i in range(N+1)]
BFSvisited=[False for i in range(N+1)]

for i in range(M):
    node,next=map(int,sys.stdin.readline().split())
    graph[node][next]=1
    graph[next][node]=1


DFS(V)
print()
BFS(V)