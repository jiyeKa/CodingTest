import sys
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(x,y):
    global count
    graph[x][y]=0
    deq=deque([(x,y)])
    while deq:
        current=deq.popleft()
        for i in range(4):
            x1=current[0]+dx[i]
            y1=current[1]+dy[i]
            if 0<=x1 and x1<n and 0<=y1 and y1<n and graph[x1][y1]==1:
                graph[x1][y1]=0
                count+=1
                deq.append((x1,y1))  

n=int(sys.stdin.readline())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

answer=[]
for x in range(n):
    for y in range(n):
        if graph[x][y]==1:
            count=1
            BFS(x,y)
            answer.append(count)
answer.sort()
print(len(answer))
[print(answer[k]) for k in range(len(answer))]