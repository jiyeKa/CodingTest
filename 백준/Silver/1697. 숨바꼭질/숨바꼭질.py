import sys
from collections import deque

def bfs(N,K):
    q=deque([(N,0)])
    visited=[False for i in range(100001)]

    while q:
        pos,sec=q.popleft()
        visited[pos]=True

        if pos==K:
            return sec
        
        for pos in (pos-1,pos+1,pos*2):
            if 0<=pos<100001 and not visited[pos]:
                visited[pos]=True
                q.append((pos,sec+1))

N,K=map(int,sys.stdin.readline().split())
print(bfs(N,K))